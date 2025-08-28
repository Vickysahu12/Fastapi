from fastapi import FastAPI,File,UploadFile
from fastapi.responses import HTMLResponse
import shutil
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Upload File</h2>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/uploadfile/")
async def upload_file(file:UploadFile=File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir,exist_ok=True)

    file_path = os.path.join(upload_dir,file.filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "saved_to": file_path}
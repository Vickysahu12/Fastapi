from fastapi import FastAPI

app = FastAPI()


#get request is used for read or fetch all data
@app.get("/video")
async def all_video():
    return{"response":"Here the child see the all the videos of todays topic"}

#read or fetch single data 
@app.get("/video/{video_id}")
async def single_video(video_id:int):
    return{"response":"math topic video is fetched", "video_id":video_id}

#post request
## create or insert data
@app.post("/video")
async def create_video(new_product:dict):
    return{"response":"new story created", "create_video":create_video}


#put request
# Update complete data
@app.put("/video/{video_id}")
async def update_video(new_updated_video:dict, video_id:int):
    return{"response":"video updated", "video_id":video_id, "new_updated_product":new_updated_video}

#patch request
# partial data updated
@app.patch("/video/{video_id}")
async def partial_video(new_updated_video:dict, video_id:int):
    return{"response":"partial video updated", "video_id":video_id, "new_updated_product":new_updated_video}


#delete request
@app.delete("/video/{video_id}")
async def delete_video(video_id:int):
    return{"response":"math topic video is deleted", "video_id":video_id}
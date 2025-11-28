from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Chat</title>
    </head>
    <body style="font-family: Arial; padding: 20px;">
        <h1>WebSocket Chat</h1>

        <label>Item ID:</label>
        <input type="text" id="item_id" value="foo">
        
        <label style="margin-left: 10px;">Token:</label>
        <input type="text" id="token" value="some-key-token">

        <button onclick="connectWS()">Connect</button>

        <hr>

        <label>Message:</label>
        <input id="messageInput" autocomplete="off">
        <button onclick="sendMessage()">Send</button>

        <ul id="messages"></ul>

        <script>
            let ws = null;

            function connectWS() {
                const itemId = document.getElementById("item_id").value;
                const token = document.getElementById("token").value;

                ws = new WebSocket(`ws://localhost:8000/ws/${itemId}?token=${token}`);

                ws.onopen = function() {
                    alert("Connected!");
                };

                ws.onmessage = function(event) {
                    const messages = document.getElementById("messages");
                    const li = document.createElement("li");
                    li.textContent = event.data;
                    messages.appendChild(li);
                };

                ws.onclose = function() {
                    alert("Disconnected");
                };
            }

            function sendMessage() {
                const input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = "";
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def home():
    return HTMLResponse(html)

@app.websocket("/ws/{item_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    item_id: str,
    token: str = Query(None)
):
    if token != "some-key-token":
        await websocket.close(code=4001)
        return

    await websocket.accept()

    await websocket.send_text(f"Connected! item_id={item_id}, token={token}")

    try:
        while True:
            msg = await websocket.receive_text()
            await websocket.send_text(f"[{item_id}] You said: {msg}")

    except WebSocketDisconnect:
        print("Client disconnected.")

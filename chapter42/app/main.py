from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import time

app = FastAPI()

active_connections = []      # To store all clients
client_ids = {}              # Map WebSocket -> unique id


# ---------------------- HTML (Frontend) ----------------------
html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <p>Your ID: <span id="cid"></span></p>

    <input id="msg" autocomplete="off"/>
    <button onclick="sendMessage()">Send</button>

    <ul id="messages"></ul>

    <script>
        var ws = new WebSocket("ws://localhost:8000/ws");
        var clientId = null;

        ws.onmessage = function(event) {
            let data = event.data;

            // First message from server contains the client ID
            if (data.startsWith("ID:")) {
                clientId = data.split(":")[1];
                document.getElementById("cid").innerText = clientId;
                return;
            }

            let li = document.createElement("li");
            li.textContent = data;
            document.getElementById("messages").appendChild(li);
        };

        function sendMessage() {
            let input = document.getElementById("msg");
            ws.send(input.value);
            input.value = "";
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get_home():
    return HTMLResponse(html)


# ---------------------- WebSocket Backend ----------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Generate unique ID for each client
    uid = str(int(time.time() * 1000))
    client_ids[websocket] = uid

    active_connections.append(websocket)
    print(f"Client {uid} connected")

    # Send this user's ID
    await websocket.send_text(f"ID:{uid}")

    # Announce join
    await broadcast(f"🔵 Client #{uid} joined.")

    try:
        while True:
            msg = await websocket.receive_text()

            # Show message to sender
            await websocket.send_text(f"You wrote: {msg}")

            # Broadcast to others
            await broadcast(f"Client #{uid} says: {msg}", sender=websocket)

    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print(f"Client {uid} disconnected")
        await broadcast(f"🔴 Client #{uid} left.")
        del client_ids[websocket]


async def broadcast(message: str, sender: WebSocket = None):
    for conn in active_connections:
        if conn != sender:
            try:
                await conn.send_text(message)
            except:
                pass



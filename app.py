from fastapi import FastAPI, WebSocket
from chatbot import diego

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = diego.get_response(data)
        await websocket.send_text(str(response))

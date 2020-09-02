from fastapi import FastAPI, WebSocket
from chatbot import Cbot

app = FastAPI()


diego = Cbot('diego')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = diego.chatbot.get_response(data)
        await websocket.send_text(str(response))


@app.websocket("/train")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await diego.train(websocket)

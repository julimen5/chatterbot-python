# client.py
import asyncio
from contextlib import suppress
import websockets

async def chat(url: str):
    async with websockets.connect(url) as websocket:
        while True:
            message = input("> ")
            await websocket.send(message)
            response = await websocket.recv()
            print(response)

async def train(url: str):
    async with websockets.connect(url) as websocket:
        # asyncio.ensure_future(keep_alive(websocket))
        while True:
            response = await websocket.recv()
            print(response)
            message = input("> ")
            await websocket.send(message)


with suppress(KeyboardInterrupt):

    # See asyncio docs for the Python 3.6 equivalent to .run().
    asyncio.run(train("ws://localhost:8000/train"))

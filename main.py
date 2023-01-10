import asyncio
import websockets


async def handler(websocket):
    while True:
        message = await websocket.recv(ping_interval=None)
        print(message)


async def main():
    async with websockets.serve(handler, "1337", ):
        await asyncio.Future()  # run forever




import aiohttp
import asyncio

async def send_message():
    async with aiohttp.ClientSession() as session:
        while True:
            message = input("message->")
            async with session.post('http://localhost:8000/p', data={'message': message}) as resp:
                pass
                # print(name + ": " + message)

if __name__ == '__main__':
    asyncio.run(send_message())
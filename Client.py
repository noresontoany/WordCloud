import aiohttp
import asyncio

async def send_message():
    async with aiohttp.ClientSession() as session:
        while True:
            message = input("Enter message: ")
            async with session.post('http://localhost:8000/p', data={'message': message}) as resp:
                print(await resp.text())

if __name__ == '__main__':
    asyncio.run(send_message())
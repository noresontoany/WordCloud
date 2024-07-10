import aiohttp
import asyncio

client_names = []
async def send_message():
    async with aiohttp.ClientSession() as session:
        name = input("name->")
        client_names.append(name)
        while True:
            message = input("Enter message: ")
            async with session.post('http://localhost:8000/p', data={'message': message}) as resp:
                print(await resp.text())
            async with session.post('http://localhost:8000/p') as resp:
                pass

if __name__ == '__main__':
    asyncio.run(send_message())
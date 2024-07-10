import time

import aiohttp_jinja2
import jinja2
from aiohttp import web

messages = []
_old_size = len(messages)
@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'messages': messages}
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=str(messages))

async def poster(request):
    d = str(request.match_info)
    d2 = await request.post()
    d3 = d2.get('message')
    if d3 is not None:
        messages.append(d3)
    return web.Response(text=d + str(messages))




app = web.Application()
app.add_routes([web.get('/', index),
                web.post('/p', poster),
                web.get('/p', handle)])
app.router.add_static('/static', path='static', name='static')

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('.'))
if __name__ == '__main__':
    web.run_app(app, port=8000)
import time

import aiohttp_jinja2
import jinja2
from aiohttp import web
import random

messages = []
words = []
_old_size = len(messages)

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'words': words}
@aiohttp_jinja2.template('text.html')
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    # words = [{'word': msg, 'weight': random.randrange(10, 20)} for msg in messages]
    return {'words': words}

async def poster(request):
    d = str(request.match_info)
    d2 = await request.post()
    d3 = d2.get('message')
    if d3 is not None:
        messages.append(d3)
        x = float(':.1f'.format(random.random()))
        words.append({'word': d3, 'weight': x})

    print(words[-1])
    return web.Response(text=d + str(messages))

async def get_chart_data(request):
    if _old_size == len(messages):
        return None
    chart_data = []
    for m in messages:
        chart_data.append({"category": m, "value": 2.1})

    # chart_data.append({"category": , "value": 2.1})
    # chart_data = [
    #     {"category": "Lorem ipsum\ndolorsit amet,\nconsectetur", "value": 2.1},
    #     {"category": "Sed do eiusmod\ntempor incididunt\nut labore et", "value": 2.2},
    #     {"category": "Duis aute irure\ndolor in\nreprehenderit", "value": 2.3},
    #     {"category": "Voluptate velit\nesse cillum dolore\neu fugiat nulla", "value": 2.1},
    #     {"category": "Excepteur sint\noccaecat cupidatat\nnon proident", "value": 2.2},
    #     {"category": "Nupidatat non proident", "value": 2},
    #     {"category": "Incididunt ut labore et", "value": 2.5},
    #     {"category": "Voluptate velit\ncillum dolore eu nulla", "value": 2.1}
    # ]
    return web.json_response(chart_data)


app = web.Application()
app.add_routes([web.get('/', index),
                web.post('/p', poster),
                web.get('/p', handle),
                web.get('/chart-data', get_chart_data)])

app.router.add_static('/static', path='static', name='static')

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('.'))
if __name__ == '__main__':
    web.run_app(app, port=8000)
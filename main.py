import time

import aiohttp_jinja2
import jinja2
from aiohttp import web
import random

all_messages = []
messages = []

@aiohttp_jinja2.template('index.html')
async def index(request):
    pass
async def poster(request):
    answer = await request.post()
    message = answer.get('message')
    if message is not None:
        messages.append(message)
        all_messages.append(message)
    return web.Response()

async def get_chart_data(request):
    chart_data = []
    for message in messages:
        chart_data.append({"category": message, "value": 2.1})
    messages.clear()
    return web.json_response(chart_data)

async def get_all_data(request):
    chart_data = []
    for message in all_messages:
        chart_data.append({"category": message, "value": 2.1})
    return web.json_response(chart_data)


app = web.Application()
app.add_routes([web.get('/', index),
                web.post('/poster', poster),
                web.get('/get-all-data', get_all_data),
                web.get('/chart-data', get_chart_data)])

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('public'))
if __name__ == '__main__':
    web.run_app(app, port=8000)
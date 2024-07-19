import aiohttp
import aiohttp_jinja2
import jinja2
from aiohttp import web


all_messages = []
clients = []
@aiohttp_jinja2.template('index.html')
async def index(request):
    pass
async def get_all_data(request):
    chart_data = []
    for message in all_messages:
        chart_data.append({"category": message, "value": 2.1})
    return web.json_response(chart_data)

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients.append(ws)
    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                chart_data = {"category": msg.data, "value": 2.1}
                all_messages.append(msg.data)
                for client in clients:
                    await client.send_json(chart_data)
    finally:
        clients.remove(ws)
    return ws



app = web.Application()
app.add_routes([web.get('/', index),
                web.get('/ws', websocket_handler),
                web.get('/get-all-data', get_all_data)])

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('public'))
if __name__ == '__main__':
    web.run_app(app, port=8000)
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
async def poster(request):
    d = str(request.match_info)
    d2 = await request.post()
    d3 = d2.get('message')
    return web.Response(text=d + str(d3))


app = web.Application()
app.add_routes([web.get('/', handle),
                web.post('/{name}', poster),
                web.get('/p', poster)])

if __name__ == '__main__':
    web.run_app(app, port=8000)
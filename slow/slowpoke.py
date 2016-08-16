import asyncio
from cowpy import cow
from aiohttp import web

async def handle(request):
    text = str(cow.Moose().milk('Yay!')).replace('<', '(').replace('>', ')')
    return web.Response(body=text.encode('utf-8'), content_type='text/plain')

async def handle_slow(request):
    await asyncio.sleep(10)
    text = str(cow.Moose().milk('Yay!')).replace('<', '(').replace('>', ')')
    return web.Response(body=text.encode('utf-8'))

async def handle_hello(request):
    return web.Response(body='hello'.encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/', handle)
app.router.add_route('GET', '/slow_cow', handle_slow)
app.router.add_route('GET', '/hello', handle_hello)

web.run_app(app)

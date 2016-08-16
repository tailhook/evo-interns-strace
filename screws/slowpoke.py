import asyncio
from cowpy import cow
import aiohttp
from aiohttp import web


async def handle(request):
    text = str(cow.Moose().milk('Yay!')).replace('<', '(').replace('>', ')')
    return web.Response(body=text.encode('utf-8'), content_type='text/plain')


async def handle_slow(request):
    await asyncio.sleep(10)
    text = str(cow.Moose().milk('Yay!')).replace('<', '(').replace('>', ')')
    return web.Response(body=text.encode('utf-8'))


async def websocket_handler(request):

    for k, v in request.headers.items():
        print(k, v)
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.tp == aiohttp.MsgType.text:
            if msg.data == 'close':
                await ws.close()
            else:
                ws.send_str(msg.data + '/answer')
        elif msg.tp == aiohttp.MsgType.error:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


app = web.Application()
app.router.add_route('GET', '/', handle)
app.router.add_route('GET', '/slow_cow', handle_slow)
app.router.add_route('GET', '/ws', websocket_handler)

web.run_app(app)

import asyncio
from websockets import connect
from websockets_proxy import proxy_connect, Proxy

async def WebsocketFactory(auth: str):
    websocket = await connect(uri='wss://pxls.space/ws', user_agent_header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36", additional_headers={ "Cookie": auth })
    print("[WS] Created websocket with auth: ", auth)
    return websocket

async def WebsocketProxyFactory(auth: str, proxy: str):
    proxy_url = Proxy.from_url(proxy)
    websocket = await proxy_connect(uri='wss://pxls.space/ws', proxy=proxy_url, user_agent_header="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36", extra_headers={ "Cookie": auth })
    print("[PROXY WS] Created proxied websocket with auth and proxy: ", auth, proxy)
    return websocket
from Util.Websocketer import WebsocketFactory, WebsocketProxyFactory
import asyncio
from websockets.asyncio.client import ClientConnection # Types
from websockets.legacy.client import WebSocketClientProtocol # Proxy Types
from websockets_proxy import proxy_connect
from Util.class_MessageHandler import WebSocketHandler
from Util.class_Canvas import canvasInstance
import time
import json
from Util.class_Queue import Queue

class Bot:
    list = []
    
    def __init__(self, auth, proxy=None):
        self.auth: str = auth
        self.proxy = proxy
        self.websocket: ClientConnection | WebSocketClientProtocol # Websocket or Proxied Websocket 
        self.queue: Queue = Queue(self)
        self.logged_in: bool
        self.login_done = asyncio.Event()
        self.username: str
        self.amount_of_pixels: int
        self.last_pixel: float = time.time()
        self.last_pixel_acknowledged: bool = True
        
    async def startBot(self):
        # Create ws
        if (not self.proxy):
            self.websocket = await WebsocketFactory(self.auth)
        else:
            self.websocket = await WebsocketProxyFactory(self.auth, self.proxy)
        # Sending to handler
        handler = WebSocketHandler(self, self.websocket)
        asyncio.create_task(handler.handle_messages())  # Keep handling messages
        await self.login_done.wait()
            
    async def kill(self):
        await self.websocket.close() 
            
    async def emit(self, type, **kwargs):
        result = {'type': type}
        # Add the extra info
        for key, value in kwargs.items():
            result[key] = value
        # To json
        result = json.dumps(result)
        await self.websocket.send(result)
        # print('sent: ', result) # Logging
    
    async def processInitialInfo(self, info: dict):
        if info["type"] != "userinfo":
            # self.kill()
            self.logged_in = False
            # For the starting process, asyncio wait
            self.login_done.set()
            print(f'[AUTH FAIL] Is the auth key correct? ({self.auth})')
            return
        #Get user
        self.username = info["username"]
        # BAN
        if info["banned"] != True:
            self.logged_in = False
            await self.kill()
            # For the starting process, asyncio wait
            self.login_done.set()
            print(f'[{self.username} BAN] Account banned, reason: ', info["banReason"])
            return
        self.logged_in = True
        self.login_done.set()
        Bot.list.append(self)
        print("Succesfuly logged in as: ", self.username)
        
    async def addPixelInTime(self, time):
        await asyncio.sleep(time)
        self.amount_of_pixels += 1
        
    async def placePixel(self, x, y, color):
        canvas_color = canvasInstance.getColor(x, y)
        
        # checks
        if (canvas_color == color or not self.logged_in):
            return
        while (self.amount_of_pixels < 1 and not self.last_pixel_acknowledged):
            print("Waiting for bigger amount and ack.")
            continue
        
        # copy behavior of web
        self.last_pixel = time.time()
        await self.emit('pixel', x=x, y=y, color=color)
        await self.emit('pixel', x=x, y=y, color=color)
        self.last_pixel_acknowledged = False
        print(self.username, ": Placing pixel at -> ", x, y, color)
        return
        
        
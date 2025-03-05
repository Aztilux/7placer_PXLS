import json
from Util.class_Canvas import canvasInstance
import Util.class_Bot as class_Bot

class WebSocketHandler:
    def __init__(self, bot, websocket):
        self.websocket = websocket
        self.bot: class_Bot.Bot = bot
        self.handlers = {
            "pixel": self.on_Pixel,
            "pixels": self.on_amountPixels,
            "users": self.on_activeUsers,
            "ping": self.on_Ping,
            "cooldown": self.on_Cooldown,
            "ACK": self.on_ACK,
            "can_undo": self.on_canUndo,
            "pixelCounts": self.on_pixelCount,
        }

    # MAIN FUNCTIONALITY
    async def handle_messages(self):
        print("Running handler...")
        await self.bot.processInitialInfo(json.loads(await self.websocket.recv()))
        async for message in self.websocket:
            await self.process_message(message)

    async def process_message(self, message):
        try:
            data = json.loads(message) # To JSON
            msg_type = data.get("type")

            if not msg_type:
                print("Invalid message: Missing 'type' field")
                return

            handler = self.handlers.get(msg_type)
            if handler:
                await handler(data)
            else:
                print(message)

        except json.JSONDecodeError:
            print("Invalid JSON received")

    # MESSAGE FUNCTIONS
    async def on_Pixel(self, data):
        for pixel in data["pixels"]:
            x = pixel["x"]
            y = pixel["y"]
            color = pixel["color"]
            canvasInstance.setColor(x, y, color)
    
    async def on_amountPixels(self, data):
        self.bot.amount_of_pixels = data["count"]
        print(f"[{self.bot.username}] Updated amount of pixels:", data["count"])
    
    async def on_activeUsers(self, data):
        canvasInstance.onlineUsers = data["count"]

    async def on_Ping(self, data):
        pass
    
    async def on_Cooldown(self, data):
        time = data["wait"]
        if (time > 0):
            print(f"[{self.bot.username}] New cooldown: ", time)
            await self.bot.addPixelInTime(time)
    
    async def on_ACK(self, data):
        self.bot.last_pixel_acknowledged = True
        print(f"[{self.bot.username}] Acknowledged pixel at", data["x"], data["y"])
    
    async def on_canUndo(self, data): # Never going to be used
        pass
    
    async def on_pixelCount(self, data): # Just stats
        pass
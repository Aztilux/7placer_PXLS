import asyncio
from Util.class_Bot import Bot
from Util.class_Canvas import canvasInstance
import Util.Botting.Image as IMG
import Util.Botting.Square as SQR
import Util.class_Queue as Q

# Load from file
# (AUTH) (http://user:pass@proxy:port)
def load_auths_and_proxies(file_path):
    pairs = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            if " " in line:
                auth, proxy = line.split(" ")
            else:
                auth = line
                proxy = None
            pairs.append({"auth": auth, "proxy": proxy})
    return pairs

# Starts by pairs
async def globalStart():
    pairsList = load_auths_and_proxies("auth_proxies.txt")
    for info in pairsList:
        bot = Bot(info["auth"], info["proxy"])
        await bot.startBot()

async def keep_alive():
    while True:
        await asyncio.sleep(3600)

async def init():
    await globalStart()
    #Functions after start
    
    # Example:
    # IMG.botImage(1223, 1060, "Cross.png")
    # await Q.Queue.globalStart()
    
    #Do not remove this
    await keep_alive()

if __name__ == '__main__':
    asyncio.run(init())
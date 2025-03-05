
# 7Placer for PXLS.SPACE

External python bot for [PXLS.SPACE](pxls.space) that allows connecting accounts through proxies.
## Adding an account

Create a file called `auth_proxies.txt` if it's not created already and add each account using this format:
- `TOKEN http://user:pass@proxy:port`
If you wish to use an account without proxy (Easy to get alt detected!):
- `TOKEN`
## Most relevant functions
Here are some basic functions of the bot:
- `Util.Botting.Image.botImage(x, y, image)`
    - Supports transparent images
    - Converts colors to canvas colors

- `Util.Botting.Square.botSquare(x_start, y_start, x_end, y_end, color)`
    - Color must be the number ingame (0-32)
- `Util.Queue.add({"x": x, "y": y, "color": color})`
    - Adds specific pixel to the global Queue
- `Util.Queue.globalStart()`
    - Starts all the logged in bots (in Bot.list)
\
Please check the code for the rest of the functions (you can get more info like canvas info, user info, etc.)



## Usage/Examples

Go to `main.py` and modify the init function, the functions must be between `keep_alive()` and `globalStart()`
```python
async def init():
    await globalStart()
    #Functions after start
    
    # Example:
    IMG.botImage(1223, 1060, "example.png")
    await Q.Queue.globalStart()
    
    #Do not remove this
    await keep_alive()
```


## Disclaimer
By using this program, I, Aztilux, will not be responsible for any banned accounts. Use at your own risk. Developers may update the page at any moment.

This program was made in a few days and there is not a big chance I will be giving much more support to it. The code is not easy to use at all.

Add me on Discord: @Azti

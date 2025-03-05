import numpy as np
from PIL import ImageColor
from Util.Requests import getBoardData, getInfo
class Canvas:

    def __init__(self):
        self.canvasArray: np.ndarray
        self.width: int
        self.height: int
        self.code: int
        self.processed: bool
        self.onlineUsers: int
        self.colors: list
        self.processCanvas()
        
        
    def processCanvas(self):
        # General Info
        info = getInfo()
        self.width = info["width"]
        self.height = info["height"]
        self.code = info["canvasCode"]
        self.__toRGBArray(info["palette"])
        # Canvas colors
        buffer = getBoardData()
        Uint8 = np.frombuffer(buffer, np.uint8).copy()
        self.canvasArray = Uint8.reshape((self.height, self.width))
        self.processed = True
        print("Canvas succesfully loaded!")
    
    def getColor(self, x: int, y: int):
        if not self.processed: 
            raise Exception('Canvas not processed yet!')
        result = self.canvasArray[y,x]
        return result
    
    def setColor(self, x, y, color):
        if not self.processed: 
            return 
        self.canvasArray[y,x] = color
        
    def __toRGBArray(self, list: list):
        result = []
        for color in list:
            hex = color["value"]
            result.append(ImageColor.getrgb(f'#{hex}'))
        self.colors = result

canvasInstance = Canvas()
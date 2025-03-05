from PIL import Image
from Util.class_Canvas import canvasInstance
from Util.class_Queue import Queue
import numpy as np
import math

def image2array(image: str):
    try:
        img = Image.open(image).convert("RGBA")
    except FileNotFoundError:
        print("Error converting image to array! File not found.")
        return
        
    array = np.array(img)
    return array

def colorDistance(rgb1: tuple, rgb2: tuple):
    #First
    r1 = int(rgb1[0])
    g1 = int(rgb1[1])
    b1 = int(rgb1[2])
    #Second
    r2 = rgb2[0]
    g2 = rgb2[1]
    b2 = rgb2[2]
    distance = math.sqrt(math.pow((r2 - r1), 2) + math.pow((g2 - g1), 2) + math.pow((b2 - b1), 2))
    return distance
    
    
    
def array2canvascolors(image_array):
    print("Converting image array to canvas color list")
    result = []
    shape = image_array.shape
    y_index = 0
    for y in image_array:
        x_index = 0
        for x in y:
            if x[3] == 0: # Skip transparent colors 
                x_index += 1
                continue
            image_color = (x[0], x[1], x[2])
            closest_distance = 999999999999999 # Big number
            color_index = 0
            closest_color = -1
            for color in canvasInstance.colors:
                distance = colorDistance(image_color, color)
                if (distance < closest_distance):
                    closest_distance = distance
                    closest_color = color_index
                color_index += 1
            result.append({"x": x_index, "y": y_index, "color": closest_color})
            x_index += 1                    
        y_index += 1
    return result    

def botImage(startX, startY, image):
    image_array = image2array(image)
    converted_colors_list = array2canvascolors(image_array)
    for pixel in converted_colors_list:
        x = pixel["x"] + startX
        y = pixel["y"] + startY
        Queue.add({"x": x, "y": y, "color": pixel["color"]})
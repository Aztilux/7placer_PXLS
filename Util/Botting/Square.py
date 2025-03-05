from Util.class_Queue import Queue

def botSquare(x_start, y_start, x_end, y_end, color):
    for y in range(y_start, y_end+1):
        for x in range(x_start, x_end+1):
            Queue.add({"x": x, "y": y, "color": color})
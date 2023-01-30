from PIL import Image
import math

"""
Load an image using his path and return the value of the shade of black for each pixel (0 to 255)
Where the data are stored using data[y_coordinate][x_coordinate]
"""

def getImageData(path:str)->list:
    img=Image.open(path)
    rawData=img.load()
    data=[]
    for y in range(img.height):
        data.append([rawData[x,y][0] for x in range(img.width)])
    return data

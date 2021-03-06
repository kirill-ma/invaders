# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 2018

@author: kirill.mareev
"""

import cv2, random
import numpy as np
import colorsys

squareSize = 50     #pixels
dimension = 7       #Canvas in blocks
padding = 1

h_w = squareSize * dimension #height = width
image = np.zeros((h_w, h_w, 3), np.uint8)

colorHalfLine = []

while 1:
    def generateColor():
        color_rgb = [c * 255 for c in colorsys.hls_to_rgb(hue, random.gauss(0.5,0.2), random.gauss(1,0.2))]
        return random.choice([color_rgb, (0,0,0)])

    def drawSquare(img, _x, _y, size, color):
        cv2.rectangle(img, (_x * size, _y * size), (_x * size + size, _y * size + size), color, -1)

    hue = random.random()
    
    for y in range(dimension - padding*2):
        for square in range((dimension - 1) // 2):
            colorHalfLine.append(generateColor())
            #print(len(colorHalfLine))
              
        for square in range((dimension - padding) // 2):
            drawSquare(image, square + padding, y + padding, squareSize, colorHalfLine[square])
            
        if (dimension % 2):
            colorHalfLine.pop()
            
        while len(colorHalfLine):
            drawSquare(image, dimension - len(colorHalfLine) - padding, y + padding, squareSize, colorHalfLine.pop())
            
    cv2.imshow("Result", image)
    k = cv2.waitKey(0)
    
    if k == 27:         # wait for ESC key to exit        
        break
    
cv2.destroyAllWindows()

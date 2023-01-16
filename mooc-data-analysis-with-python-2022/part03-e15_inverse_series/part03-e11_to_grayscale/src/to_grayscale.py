#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    def gray_image(image):
        R,G,B = image[:,:,0],image[:,:,1],image[:,:,2]
        result = R * 0.2126 + G * 0.7152 + B * 0.0722
        return result

    if isinstance(image,str):
        imager = plt.imread(image)
        result = gray_image(imager)
        return result
    
    else:
        result= gray_image(image)
        return result

def to_red(image):
    def calc(image):
        image[:,:,1] = 0
        image[:,:,2] = 0
        return image

    if isinstance(image,str):
        image = plt.imread(image)
        res = calc(image)
        return res

    else:
        res = calc(image)
        return res

def to_green(image):
    def calc(image):
        image[:,:,0] = 0
        image[:,:,2] = 0
        return image

    if isinstance(image,str):
        image = plt.imread(image)
        res = calc(image)
        return res

    else:
        res = calc(image)
        return res
  
def to_blue(image):
    def calc(image):
        image[:,:,0] = 0
        image[:,:,1] = 0
        return image

    if isinstance(image,str):
        image = plt.imread(image)
        res = calc(image)
        return res

    else:
        res = calc(image)
        return res

def main():
    im = "src/painting.png"
    res = to_grayscale("src/painting.png" )
    plt.imshow(res)
    plt.gray()
    fig = plt.figure()
    plt.subplot(3,1,1)
    plt.imshow(to_red(im))
    plt.subplot(3,1,2)
    plt.imshow(to_green(im))
    plt.subplot(3,1,3)
    plt.imshow(to_blue(im))
    plt.show()

if __name__ == "__main__":
    main()

import cv2
import numpy as np

def GetGrayScaleImage(path):
    img = cv2.imread(path, 0)
    cv2.imshow("", img)
    cv2.waitKey(0)
    return img

def Erosion(image, filt):
    buffer = image.copy()
    hi = image.shape[0]
    wi = image.shape[1]
    hf = filt.shape[0]
    wf = filt.shape[1]

    print("image height: ", hi)
    print("image width: ", wi)
    print("filt height: ", hf)
    print("filt width: ", wf)
    
    return buffer

GetGrayScaleImage("image.jpg")
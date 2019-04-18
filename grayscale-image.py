import cv2
import numpy as np
import sys

def GetGrayScaleImage(path):
    img = cv2.imread(path, 0)
    return img

def Erosion(image, filt, centerRow, centerColumn):
    buffer = image.copy()
    hi = image.shape[0]
    wi = image.shape[1]
    hf = filt.shape[0]
    wf = filt.shape[1]

    print("image height: ", hi)
    print("image width: ", wi)
    print("filt height: ", hf)
    print("filt width: ", wf)

    for loop in range(0, hi):
        for loop2 in range(0, wi):
             clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn, 255)
             buffer[loop,loop2] = np.amin(clone)
    
    return buffer

def Dilation(image, filt, centerRow, centerColumn):
    buffer = image.copy()
    hi = image.shape[0]
    wi = image.shape[1]
    hf = filt.shape[0]
    wf = filt.shape[1]

    print("image height: ", hi)
    print("image width: ", wi)
    print("filt height: ", hf)
    print("filt width: ", wf)

    for loop in range(0, hi):
        for loop2 in range(0, wi):
             clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn, 0)
             buffer[loop,loop2] = np.amax(clone)
    
    return buffer

def Opening(image, filt, centerRow, centerColumn):
    image2 = Erosion(image, filt, 1, 1)
    image2 = Dilation(image2, filt, 1, 1)
    return image2

def Closing(image, filt, centerRow, centerColumn):
    image2 = Dilation(image, filt, 1, 1)
    image2 = Erosion(image2, filt, 1, 1)
    return image2

def GetShapes(parent, child, atRow, atColumn, centerRow, centerColumn, default):
    buffer = child.copy()
    hp = parent.shape[0]
    wp = parent.shape[1]
    hc = child.shape[0]
    wc = child.shape[1]

    for loop in range(0, hc):
        for loop2 in range(0, wc):
            if atRow - (centerRow - loop) < 0 or atRow + (loop - centerRow) >= hp or atColumn - (centerColumn - loop2) < 0 or atColumn + (loop2 - centerColumn) >= wp:
                buffer[loop,loop2] = default
                continue

            if child[loop, loop2] == 1:
                buffer[loop,loop2] = parent[atRow - (centerRow - loop), atColumn - (centerColumn - loop2)]
            else:
                buffer[loop,loop2] = default

    return buffer
def test_erosion():
    filt = 	np.asarray([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])

    image = GetGrayScaleImage("image.jpg")
    image2 = Erosion(image, filt, 1, 1)
    cv2.imwrite("image-erosion.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_dilation():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

    image = GetGrayScaleImage("image.jpg")
    image2 = Dilation(image, filt, 1, 1)
    cv2.imwrite("image-dilation.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_opening():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    image = GetGrayScaleImage("image.jpg")
    image2 = Opening(image, filt, 1, 1)
    cv2.imwrite("image-opening.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_closing():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    image = GetGrayScaleImage("image.jpg")
    image2 = Closing(image, filt, 1, 1)
    cv2.imwrite("image-closing.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def main():
    task = sys.argv[1]
    if task == "opening":
        test_opening()
        return
    
    if task == "closing":
        test_closing()
        return

    if task == "erosion":
        test_erosion()
        return

    if task == "dilation":
        test_dilation()
        return

main()
        
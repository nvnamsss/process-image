import cv2
import numpy as np

def GetGrayScaleImage(path):
    img = cv2.imread(path, 0)
    cv2.imshow("", img)
    cv2.waitKey(0)
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
             clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn)
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
             clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn)
             buffer[loop,loop2] = np.amax(clone)
    
    return buffer

def Opening(image, filt, centerRow, centerColumn):
    image = GetBinaryImage("image.jpg", 128)
    image2 = Erosion(image, filt, 1, 1)
    image2 = Dilation(image2, filt, 1, 1)
    return image2

def Closing(image, filt, centerRow, centerColumn):
    image = GetBinaryImage("image.jpg", 128)
    image2 = Dilation(image, filt, 1, 1)
    image2 = Erosion(image2, filt, 1, 1)
    return image2

def GetShapes(parent, child, atRow, atColumn, centerRow, centerColumn):
    buffer = child.copy()
    hp = parent.shape[0]
    wp = parent.shape[1]
    hc = child.shape[0]
    wc = child.shape[1]

    boundH = atRow - centerRow
    boundW = atColumn - centerColumn
    
    if atRow - centerRow < 0 or atColumn - centerColumn < 0 or atRow + (hc - centerRow) >= hp or atColumn + (wc - centerColumn) >= wp:
        print('atRow {0} atColumn {1} centerRow {2} centerColumn {3} hp {4} wp {5} hc {6} wc {7}'.format(atRow, atColumn, centerRow, centerColumn, hp, wp, hc, wc))
        return np.array([])

    for loop in range(0, hc):
        for loop2 in range(0, wc):
            if atRow - (centerRow - loop) < 0 or atRow + (loop - centerRow) > hp
                 or atColumn - (centerColumn - loop2) < 0 or atColumn + (loop2 - centerColumn) > wp:
                buffer[loop,loop2] = 255
                continue

            if child[loop, loop2] == 1:
                buffer[loop,loop2] = parent[atRow - (centerRow - loop), atColumn - (centerColumn - loop2)]
            else:
                buffer[loop,loop2] = 255

    return buffer

def main():
    task = sys.argv[1]
    if task == "opening"
        test_opening()
        return
    
    if task == "closing"
        test_closing()
        return

    if task == "erosion":
        test_erosion()
        return

    if task == "dilation":
        test_dilation()
        return
        
GetGrayScaleImage("image.jpg")
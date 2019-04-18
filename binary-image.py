import cv2
import numpy as np
import sys

def GetBinaryImage(path, threshold):
    img = cv2.imread(path, 0)
    (thresh, img_binary) = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return img_binary

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
            # print(image[loop,loop2])
            if image[loop,loop2] == 0:
                isClear = False
                clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn)
                #print(type(clone))
                if clone.shape[0] == 0:
                    buffer[loop, loop2] = 255
                    continue

                for loop3 in range(0, hf):
                    for loop4 in range(0, wf):
                        if clone[loop3,loop4] != filt[loop3,loop4]:
                            isClear = True
                            break

                if isClear:
                    buffer[loop,loop2] = 255

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
            # print(image[loop,loop2])
            if image[loop,loop2] == 0:
                clone = GetShapes(image, filt, loop, loop2, centerRow, centerColumn)
                #print(type(clone))
                if clone.shape[0] == 0:
                    continue

                for loop3 in range(0, hf):
                    for loop4 in range(0, wf):
                        buffer[loop + loop3, loop2 + loop4] = filt[loop3, loop4]

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
    
    if atRow - centerRow < 0 or atColumn - centerColumn < 0 or atRow + (hc - centerRow) >= hp or atColumn + (wc - centerColumn) >= wp:
        print('atRow {0} atColumn {1} centerRow {2} centerColumn {3} hp {4} wp {5} hc {6} wc {7}'.format(atRow, atColumn, centerRow, centerColumn, hp, wp, hc, wc))
        return np.array([])

    for loop in range(0, hc):
        for loop2 in range(0, wc):
            buffer[loop,loop2] = parent[atRow - (centerRow - loop), atColumn - (centerColumn - loop2)]

    return buffer

def test_erosion():
    filt = 	np.asarray([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])

    image = GetBinaryImage("image.jpg", 128)
    image2 = Erosion(image, filt, 1, 1)
    cv2.imwrite("image-erosion.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_dilation():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

    image = GetBinaryImage("image.jpg", 128)
    image2 = Dilation(image, filt, 1, 1)
    cv2.imwrite("image-dilation.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_opening():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    image = GetBinaryImage("image.jpg", 128)
    image2 = Opening(image, filt, 1, 1)
    cv2.imwrite("image-opening.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

def test_closing():
    filt = 	np.asarray([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    image = GetBinaryImage("image.jpg", 128)
    image2 = Closing(image, filt, 1, 1)
    cv2.imwrite("image-closing.jpg", image2)
    cv2.imwrite("image-binary.jpg", image)
    print("white count before: ", cv2.countNonZero(image))
    print("white count after: ", cv2.countNonZero(image2))

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

main()
import numpy as np
import cv2 as cv
import sys

def find_aruco_corners(corners, ids):
    corner_markers = [np.median(corners[int(np.where(ids == 30)[0])][0], axis = 0).astype(int).tolist(),
                      np.median(corners[int(np.where(ids == 0)[0])][0], axis = 0).astype(int).tolist(),
                      np.median(corners[int(np.where(ids == 34)[0])][0], axis = 0).astype(int).tolist(),
                      np.median(corners[int(np.where(ids == 4)[0])][0], axis = 0).astype(int).tolist()]
    
    return corner_markers

def get_corner_pixels(img):
    return [[0,0],
            [img.shape[1]-1, 0],
            [0, img.shape[0]-1],
            [img.shape[1]-1, img.shape[0]-1]]


dic = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

escanor = cv.imread(sys.argv[1], 1)
escanor = cv.cvtColor(escanor, cv.COLOR_BGR2RGB)
orig = get_corner_pixels(escanor)

while True:
    ret, image = cap.read()
    
    corners, ids, _ = cv.aruco.detectMarkers(image, dic)
    if ids is not None:
        if [0] in ids and [4] in ids and [30] in ids and [34] in ids:
            dest = find_aruco_corners(corners, ids)
            h = cv.findHomography(np.array(orig), np.array(dest))[0]
            final = cv.warpPerspective(escanor, h, (image.shape[1], image.shape[0]))
            
            print(final > 0)

            final[final == 0] = image[final == 0]


            cv.imshow('frame', final)
        else:
            cv.imshow('frame', image)
    else:
        cv.imshow('frame', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
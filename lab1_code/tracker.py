"""code mostly adapted from
https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html

used as references for cv2.findContours
https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#gae4156f04053c44f886e387cff0ef6e08
https://docs.opencv.org/3.4.14/d9/d8b/tutorial_py_contours_hierarchy.html
"""

import cv2 as cv
import numpy as np

#

def bounding():
    cap = cv.VideoCapture(0)
    while(1):
        # Take each frame
        _, frame = cap.read()
        #
        # Convert BGR to HSV
        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        # define range of blue color in HSV
        lower = np.array([100,120,120])
        upper = np.array([150,255,255])
        # define range of blue color in RGB
        #lower = np.array([130,80,80])
        #upper = np.array([255,120,120])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(frame, lower, upper)
        #
        contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv.boundingRect(cnt)
            frame = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv.imshow('box',frame)
        #esc to stop
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()
    
def main():
    bounding()
if __name__ == "__main__":
    print(__doc__)
    main()
    cv.destroyAllWindows()
    
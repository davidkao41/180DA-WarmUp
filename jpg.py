#!/usr/bin/python
import cv2
import sys
image = cv2.imread(str(sys.argv[1])+".jpg", 1)
cv2.imwrite(str(sys.argv[1])+".png", image)
    

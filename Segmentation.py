#Signflow
#Importing dependencies
import cv2
import numpy
import pandas as pd
def crop(img, x1, x2, y1, y2, scale):
    crp=img[y1:y2,x1:x2]
    crp=resize(crp,((scale, scale))) 
    return crp
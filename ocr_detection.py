
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import cv2
import time
import easyocr
import numpy as np
import matplotlib.pyplot as plt


## Infrastructure
reader = easyocr.Reader(['en'], gpu=True)
###=> Use Webcam
vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture("numplate.mp4")
skip_frame = True


while(True):
    currTime = time.time()
    ret, img = vid.read()

    ## Break down
    ##=> convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    ##=> Take OCR module and read text from grayscale
    results = reader.readtext(gray)
    text = ""

    for res in results:
        text += res[1] + " "
    cv2.putText(img, text, (50, 70), cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 255), 2)

    ### Frame Per Seconds
    prevTime = 0
    fps = 1/(prevTime - currTime)
    prevTime = time.time()
    cv2.line(img, (20, 25), (127, 25), [85, 45, 255], 30)
    cv2.putText(img, text, (50, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (50, 50, 255), 2)
    cv2.imshow("results", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(fps)
    print(text)
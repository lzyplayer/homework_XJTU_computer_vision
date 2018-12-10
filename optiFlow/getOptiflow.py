# -*- coding: utf-8 -*-
# @Time     : 2018/12/10 16:55
# @Author   : vickylzy
# original code:"https://docs.opencv.org/4.0.0-beta/d7/d8b/tutorial_py_lucas_kanade.html"

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('scienceP21.avi')
ret, frame = cap.read()
if frame is not None:
    cv.imshow('test', frame)

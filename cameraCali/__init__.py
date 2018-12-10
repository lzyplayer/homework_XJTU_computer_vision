# -*- coding: utf-8 -*-
# @Time     : 2018/12/10 11:15
# @Author   : vickylzy
import cv2 as cv
from cameraCali.getCorner import getCorner

if __name__ == '__main__':

    obj_p, img_p, img_shape = getCorner('../shots/*.jpg', 6, 8)
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(obj_p, img_p, img_shape, None, None)
    img = cv.imread('../shots/02.jpg')
    h, w = img.shape[:2]
    newmtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    result = cv.undistort(img, mtx, dist, None, newmtx)
    x, y, w, h = roi
    result = result[y:y + h, x:x + w]
    cv.imshow('result',result)
    cv.waitKey()


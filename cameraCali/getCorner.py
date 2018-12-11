# -*- coding: utf-8 -*-
# @Time     : 2018/12/10 11:16
# @Author   : vickylzy
# original code:"https://docs.opencv.org/trunk/dc/dbb/tutorial_py_calibration.html"


import numpy as np
import cv2 as cv
import glob


def getCorner(filename, pw, ph):
    # filename = '../shots/*.jpg'
    # pw = 6
    # ph = 8
    # 迭代终止条件 第一参数为类型选择 （本例为 精准度达0.01 或迭代次数满足30 时退出）
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 30, 0.01)

    # 准备三维点坐标
    objp = np.zeros(((pw * ph), 3), np.float32)
    objp[:, :2] = np.mgrid[0:ph, 0:pw].T.reshape(-1, 2)  # -1代表不关系行数

    obj_points = []  # 3d point in real world space
    img_points = []  # 2d points in image plane.

    images = glob.glob(filename)  # '../shots/*.jpg'
    for frame in images:
        img = cv.imread(frame)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        ret, corners = cv.findChessboardCorners(gray, (8, 6), None)

        if ret:
            obj_points.append(objp)
            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  # 第三个为查找区间 第四个为不查找区(无)
            """
            Parameters
        image	Input single-channel, 8-bit or float image.
        corners	Initial coordinates of the input corners and refined coordinates provided for output.
        winSize	Half of the side length of the search window. For example, if winSize=Size(5,5) , then a (5∗2+1)×(5∗2+1)=11×11 search window is used.
        zeroZone	Half of the size of the dead region in the middle of the search zone over which the summation in the formula below is not done. It is used sometimes to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1) indicates that there is no such a size.
        criteria	Criteria for termination of the iterative process of corner refinement. That is, the process of corner position refinement stops either after criteria.maxCount iterations or when the corner position moves by less than criteria.epsilon on some iteration.
            """
            img_points.append(corners)
            cv.drawChessboardCorners(img, (ph, pw), corners2, ret)
            cv.namedWindow('img', cv.WINDOW_NORMAL)
            cv.imshow('img', img)
            cv.waitKey(100)
            # input("wait command")
    cv.destroyAllWindows()
    img_shape = gray.shape[::-1]
    return obj_points, img_points, img_shape

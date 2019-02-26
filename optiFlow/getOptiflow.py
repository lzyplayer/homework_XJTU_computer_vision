# -*- coding: utf-8 -*-
# @Time     : 2018/12/10 16:55
# @Author   : vickylzy
# original code:"https://docs.opencv.org/4.0.0-beta/d7/d8b/tutorial_py_lucas_kanade.html"

import numpy as np
import cv2 as cv
import os

target_name = '../video/car2.flv'  # car1.flv.
if not os.path.exists(target_name):
    raise Exception('file not exists!', target_name)
cap = cv.VideoCapture(target_name)
# 测试视频读取        # frame.shape  (480 580+-)
# ret, frame = cap.read()
# if frame is not None:
#     cv.namedWindow('pool', cv.WINDOW_NORMAL)
#     cv.imshow('pool', frame)
#     cv.waitKey()
#     1==1
# 角点参数
feature_param = dict(maxCorners=50,
                     qualityLevel=0.2,
                     minDistance=7,
                     blockSize=7,
                     mask=None)
# LK法参数
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# 创立随机颜色带共100条(最多100点)
color = np.random.randint(0, 255, (100, 3))
# 初始帧寻找优秀角点
ret, ori_frame = cap.read()
ori_gray = cv.cvtColor(ori_frame, cv.COLOR_BGR2GRAY)
ori_corners = cv.goodFeaturesToTrack(ori_gray, **feature_param)

# 画布
mask = np.zeros_like(ori_frame)  # 函数返回一个等大小0矩阵
print('Initial completed on ', target_name)
print('found', ori_corners.shape[0], 'corner points...')
print('----------------start tracking----------------')
frameN = 1
while True:
    # 获取当前帧
    frameN = frameN + 1
    print('processing frame', frameN)
    ret, curr_frame = cap.read()
    if not ret:
        print('----------------done tracking!----------------')
        print("'enter' to quit")
        cv.waitKey()
        break
    curr_gray = cv.cvtColor(curr_frame, cv.COLOR_BGR2GRAY)
    # curr_corner_test = cv.goodFeaturesToTrack(curr_gray, **feature_param)  # 和其特征角点(optional)
    # LK光流
    curr_corners, status, err = cv.calcOpticalFlowPyrLK(ori_gray, curr_gray, ori_corners, None, **lk_params)
    # (ori_gray, curr_gray, ori_corners, curr_corner_test , **lk_params)

    # 选择匹配上点
    match_ori = ori_corners[status == 1]
    match_curr = curr_corners[status == 1]

    # 展示路径
    for i, (new_cor, ori_cor) in enumerate(zip(match_curr, match_ori)):
        a, b = new_cor.ravel()  # 返回一维数据，new_cor内嵌套维度过高
        c, d = ori_cor.ravel()
        # mask = cv.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv.circle(curr_frame, (a, b), 4, color[i].tolist(), -1)
    img = cv.add(curr_frame, mask)
    cv.imshow('frame', img)
    k = cv.waitKey()  # 帧等待时间100
    # if k == 27: & 0xff
    #     break
    # Now update the previous frame and  previous points

    ori_gray = curr_gray.copy()
    ori_corners = match_curr.reshape(-1, 1, 2)
cv.destroyAllWindows()
cap.release()

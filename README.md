# homework for XJTU-CV

- ### Camera Calibrate ------  cameraCali/\_\_init\_\_.py

- ### Optical Flow ----- optiFlow/getOptiflow.py

1. #### 手持相机校正与标定

   - 目标
     - 光学透镜具有固有透视失真，在手持相机模型中表现为径向畸变
     - 切向畸变，这是由于透镜与成像平面不可能绝对平行造成的。这种畸变会造成图像中的某些点看上去的位置会比我们认为的位置要近一些
     - 修正以上畸变

   ![calib_radial.jpg](https://docs.opencv.org/trunk/calib_radial.jpg) 

   - 成像过程
     - 要将真实世界中一点$P = \left( {X,Y,Z} \right)$转化为二维图像中一点$p = \left( {u,v} \right)$

     - 从__世界坐标系__到__相机坐标系__到__成像坐标系__到__图像像素坐标系__

     - $$
       s\left(\begin{array}{c}\mu\\ \nu \\ 1\end{array}\right) = \left[\begin{array}{ccc}\alpha & 0 &c_x \\ 0 & \beta & c_y \\ 0 & 0 & 1\end{array}\right] \left[\begin{array}{cccc}f&0&0&0\\0&f&0&0\\0&0&1&0\end{array}\right] \left[\begin{array}{cc}R&t\\0^T&1\end{array}\right] \left(\begin{array}{c}X\\Y\\Z\\1\end{array}\right) \\
       = \left[\begin{array}{cccC}f_x&0&c_x&0\\0&f_y&c_y&0\\0&0&1&0\end{array}\right]\left[\begin{array}{cc}R&t\\0^T&1\end{array}\right] \left(\begin{array}{c}X\\Y\\Z\\1\end{array}\right)
       $$

       

     - 其中$K = \left[\begin{array}{ccc}f_x&0&c_x\\0&f_y&c_y\\0&0&1\end{array}\right]$是相机的内参矩阵，$f_x,f_y$为焦距$f$乘以$x,y$方向上单位距离像素个数，$c_x,c_y$为相机图片$x,y$方向上像素的一半
   - 张氏标定法
     - 采用黑白棋盘标定板作为拍摄对象，寻找棋盘板所在平面$G_1$与相机成像平面$G_2$之间的关系，通过角点检测可以找到棋盘各个角点在图像中的像素位置，又已知每个角点在实际世界空间中的位置关系，依次寻找两平面的单应关系

     - 图像像素坐标系点$p$与棋盘平面坐标系对应点$P$关系为$p = K[R|t]P$，令$H = K[R|t]$，称H为单应矩阵，即就是联系了

       

2. #### null
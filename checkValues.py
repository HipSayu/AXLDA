import cv2
import numpy as np


def nothing(x):
    pass


frame = cv2.imread('D:\workspace\DA Python XLA\Image\Training_1.jpg')
height, width = frame.shape[:2]
new_height = int(height / 2)
new_width = int(width / 2)

cv2.namedWindow("Trackbars")
cv2.resizeWindow('Trackbars', 500, 500)
cv2.createTrackbar("L - H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 15, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 15, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 250, 255, nothing)

cv2.createTrackbar("L - YC", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - b", "Trackbars", 139, 255, nothing)
cv2.createTrackbar("L - CR", "Trackbars", 108, 255, nothing)
cv2.createTrackbar("U - YC", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - b", "Trackbars", 189, 255, nothing)
cv2.createTrackbar("U - CR", "Trackbars", 136, 255, nothing)

while True:
    HSV_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    YCbCr_image = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    l_yc = cv2.getTrackbarPos("L - YC", "Trackbars")
    l_b = cv2.getTrackbarPos("L - b", "Trackbars")
    l_cr = cv2.getTrackbarPos("L - CR", "Trackbars")
    u_yc = cv2.getTrackbarPos("U - YC", "Trackbars")
    u_b = cv2.getTrackbarPos("U - b", "Trackbars")
    u_cr = cv2.getTrackbarPos("U - CR", "Trackbars")
    
    lower_HSV_values = np.array([l_h, l_s, l_v], dtype="uint8")
    upper_HSV_values = np.array([u_h, u_s, u_v], dtype="uint8")
    
    lower_YCbCr_values = np.array((l_yc, l_b, l_cr), dtype="uint8")
    upper_YCbCr_values = np.array((u_yc,u_b,u_cr), dtype="uint8")
    
    
    mask_YCbCr = cv2.inRange(YCbCr_image, lower_YCbCr_values, upper_YCbCr_values)
    mask_HSV = cv2.inRange(HSV_image, lower_HSV_values, upper_HSV_values)

    skin_mask = cv2.add(mask_HSV, mask_YCbCr)
    
    image_foreground = cv2.erode(skin_mask, None, iterations=3)
    dilated_binary_image = cv2.dilate(skin_mask, None, iterations=3)
    _, image_background = cv2.threshold(dilated_binary_image, 1, 128, cv2.THRESH_BINARY)
    image_marker = cv2.add(image_foreground, image_background)
    image_marker32 = np.int32(image_marker)
    image_marker32 = cv2.watershed(frame, image_marker32)
    m = cv2.convertScaleAbs(image_marker32)
    _, image_mask = cv2.threshold(m, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    skin = cv2.bitwise_and(frame, frame, mask=image_mask)
  


    cv2.imshow("result", skin)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows() 
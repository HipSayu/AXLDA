import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh từ file
img = cv2.imread('D:\workspace\DA Python XLA\Image\skin.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng ngưỡng để gán giá trị 0 cho các điểm ảnh nhỏ hơn 50
_, thresholded = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng ngưỡng
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(thresholded, 'gray'), plt.title('Thresholded Image')
cv2.imwrite('D:/thresholded.jpg', thresholded)
plt.show()

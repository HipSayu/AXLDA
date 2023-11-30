import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file
img = cv2.imread('D:\workspace\DA Python XLA\Image\Imagethresholded.jpg', cv2.IMREAD_GRAYSCALE)

# Tạo structuring element (kernel) cho phép toán opening với bán kính 1
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))  # MORPH_ELLIPSE tạo kernel hình elip

# Thực hiện phép toán opening
opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng opening
plt.subplot(1, 2, 1), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(opened_img, 'gray'), plt.title('Opened Image')
cv2.imwrite('D:/opened_img.jpg', opened_img)
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file
img = cv2.imread('D:\workspace\DA Python XLA\Image\opened_img.jpg', cv2.IMREAD_GRAYSCALE)

# Ngưỡng để tạo ảnh nhị phân
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Tạo structuring element (kernel) cho phép toán closing
kernel = np.ones((1, 1), np.uint8)  # Một kernel hình vuông 5x5, bạn có thể thay đổi kích thước

# Thực hiện phép toán dilation để điền các lỗ trống
filled_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('D:/filled_img.jpg', filled_img)
# Hiển thị ảnh gốc, ảnh nhị phân và ảnh sau khi fill holes
plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(binary_img, 'gray'), plt.title('Binary Image')
plt.subplot(133), plt.imshow(filled_img, 'gray'), plt.title('Filled Holes Image')

plt.show()

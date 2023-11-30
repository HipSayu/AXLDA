import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh từ file, convert sang gray
img = cv2.imread('D:\skinImage.jpg', cv2.IMREAD_GRAYSCALE)
img= cv2.equalizeHist(img)
for i in range (0, 20):
    # Áp dụng ngưỡng để gán giá trị 0 cho các điểm ảnh nhỏ hơn 50
    _, thresholded = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

    # Tạo structuring element (kernel) cho phép toán opening với bán kính 1
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))  # MORPH_ELLIPSE tạo kernel hình elip

    # Thực hiện phép toán opening
    opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel1)

    # Tạo structuring element (kernel) cho phép toán closing
    kernel2 = np.ones((1, 1), np.uint8)  # Một kernel hình vuông 1x1, bạn có thể thay đổi kích thước

    # Thực hiện phép toán dilation để điền các lỗ trống
    filled_img = cv2.morphologyEx(opened_img, cv2.MORPH_CLOSE, kernel2)


    #Tạo structuring element (kernel) cho phép toán opening với bán kính 6
    kernel_size = 6
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

    # Thực hiện phép toán opening
    opened_img = cv2.morphologyEx(filled_img, cv2.MORPH_OPEN, kernel)
    img = opened_img
    
img1 = cv2.imread('D:\skinImage.jpg', cv2.IMREAD_GRAYSCALE)
img1= cv2.equalizeHist(img1)

# plt.subplot(1, 2, 1), plt.imshow(img1, 'gray'), plt.title('Original Image')
# # cv2.imwrite('D:/opened_img19.jpg', img)
# plt.subplot(1, 2, 2), plt.imshow(img, 'gray'), plt.title('mask')
# plt.show()



# Kiểm tra xem ảnh có cùng kích thước không
if img1.shape == opened_img.shape:
    # Thực hiện phép nhân pixel-wise
    masked_img = cv2.bitwise_and(img1, img1, mask=opened_img)
    plt.imshow(masked_img, cmap='gray'), plt.title('Multiplied Image')
    plt.show()
    cv2.imwrite('D:/masked.jpg', masked_img)
else:
    print("Images have different sizes. Make sure both images have the same dimensions.")



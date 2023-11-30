import cv2
import numpy as np

# Đọc ảnh nhị phân
binary_image = cv2.imread('D:/masked.jpg', cv2.IMREAD_GRAYSCALE)

# Tìm các vùng kết nối
num_labels, labels = cv2.connectedComponents(binary_image)

# Hàm để kiểm tra và cắt ảnh con
def process_and_save_component(label, component_mask):
    # Lấy bounding box của contour
    x, y, w, h = cv2.boundingRect(component_mask)

    # Kiểm tra kích thước của ảnh con
    aspect_ratio = w / h  # Tỉ lệ khung hình
    if 45 <= w <= 500 and 45 <= h <= 500 and 0.45< aspect_ratio and h/w !=56/48 :
        # Cắt và lưu ảnh con
        cropped_image = binary_image[y:y+h, x:x+w]
        cv2.imwrite(f'D:\Image\cropped_image_{label}.png', cropped_image)
        print(f"Processed and Kept component {label} - Width: {w}, Height: {h}, Aspect Ratio: {aspect_ratio}")
    else:
        print(f"Skipped component {label} - Width: {w}, Height: {h}, Aspect Ratio: {aspect_ratio}")

# Lặp qua từng vùng kết nối
for label in range(1, num_labels):  # Bắt đầu từ 1 để bỏ qua nền
    component_mask = np.uint8(labels == label)
    
    # Gọi hàm xử lý cho mỗi vùng kết nối
    process_and_save_component(label, component_mask)

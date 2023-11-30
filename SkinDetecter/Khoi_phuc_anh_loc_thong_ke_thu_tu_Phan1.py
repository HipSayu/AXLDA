import numpy as np
import cv2
import matplotlib.pyplot as plt


def Loc_TKTT_max(img, ksize):
    m, n = img.shape
    img_ket_qua_anh_loc_max = np.zeros([m, n])
    h=(ksize -1) // 2
    padded_img = np.pad(img, (h, h), mode='reflect')
    for i in range(m):
        for j in range(n):
            vung_anh_kich_thuoc_k = padded_img[i:i+ksize,j:j+ksize]
            gia_tri_Max = np.max(vung_anh_kich_thuoc_k)
            img_ket_qua_anh_loc_max[i, j] = gia_tri_Max
    return img_ket_qua_anh_loc_max

def Loc_TKTT_min(img, ksize):
    m, n = img.shape
    img_ket_qua_anh_loc_min = np.zeros([m, n])
    h=(ksize -1) // 2
    padded_img = np.pad(img, (h, h), mode='reflect')
    for i in range(m):
        for j in range(n):
            vung_anh_kich_thuoc_k = padded_img[i:i+ksize,j:j+ksize]
            gia_tri_Min = np.min(vung_anh_kich_thuoc_k)
            img_ket_qua_anh_loc_min[i, j] = gia_tri_Min
    return img_ket_qua_anh_loc_min

def Loc_TKTT_trung_vi(img, ksize):
    m, n = img.shape
    img_ket_qua_anh_loc_Trung_vi= np.zeros([m, n])
    h=(ksize -1) // 2
    padded_img = np.pad(img, (h, h), mode='reflect')
    for i in range(m):
        for j in range(n):
            vung_anh_kich_thuoc_k = padded_img[i:i+ksize,j:j+ksize]
            gia_tri_TV = np.median(vung_anh_kich_thuoc_k)
            img_ket_qua_anh_loc_Trung_vi[i, j] = gia_tri_TV
    return img_ket_qua_anh_loc_Trung_vi

if __name__ == "__main__":

    img_nhieu_hat_tieu = cv2.imread('D:\workspace\DA Python XLA\Image\.jpg', 0)
   
    ksize_1 = 3 # Để lọc ảnh nhiễu muối, ảnh nhiễu hạt tiêu
    ksize_2 =7  # Để lọc ảnh nhiễu muối tiêu
    
    
    
    img_KQ_Max1 = Loc_TKTT_max(img_nhieu_hat_tieu, 3)
    img_KQ_Max2 = Loc_TKTT_max(img_KQ_Max1, 3)
    img_KQ_Max3 = Loc_TKTT_max(img_KQ_Max2, 3)
    img_KQ_Max4 = Loc_TKTT_max(img_KQ_Max3, 3)
    img_KQ_Max5 = Loc_TKTT_max(img_KQ_Max4, 3)
    img_KQ_Max6 = Loc_TKTT_max(img_KQ_Max5, 3)
   

    fig = plt.figure(figsize=(16, 9))     # Thiết lập vùng (cửa sổ) vẽ
    (ax1, ax2) = fig.subplots(1, 2)        # Thiết lập 2 vùng con ax1, ax2
    ax1.imshow(img_nhieu_hat_tieu, cmap='gray')      # Hiển thị ảnh gốc vùng ax1
    ax1.set_title("ảnh gốc bị nhiễu hạt tiêu")             # Thiết lập tiêu đề vùng ax1
    ax1.axis("off")

    ax2.imshow(img_KQ_Max6, cmap='gray')       # Hiển thị ảnh sau khi lọc
    ax2.set_title("ảnh sau khi lọc TKTT Max") # Thiết lập tiêu đề vùng ax2
    ax2.axis("off")

    plt.show()
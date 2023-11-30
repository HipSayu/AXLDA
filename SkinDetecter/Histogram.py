import cv2 
import matplotlib.pyplot as plt


img = cv2.imread(r'D:\workspace\DA Python XLA\Image\Training_1.jpg', 0)
img_equalized = cv2.equalizeHist(img)
cv2.imwrite('D:/LolHis.jpg', img_equalized)

fig = plt.figure(figsize=(16, 9))

(ax1, ax2) , (ax3, ax4) = fig.subplots(2, 2)





ax1.imshow(img, cmap='gray')
ax1.set_title('anh goc')

ax2.hist(img)
ax2.set_title('histogram anh goc')


ax3.imshow(img_equalized, cmap='gray')
ax3.set_title('img_equalized')



ax4.hist(img_equalized)
ax4.set_title('histogram img_equalized')
plt.show()



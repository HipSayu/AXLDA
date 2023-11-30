import cv2
import numpy as np
import os

# Read the image and template
image = cv2.imread('D:\masked.jpg', cv2.IMREAD_GRAYSCALE)
images = cv2.imread('D:\workspace\DA Python XLA\Image\Training_1.jpg')
# template = cv2.imread('D:\Image\cropped_image_176.png', cv2.IMREAD_GRAYSCALE)
folder_path= 'D:\Image'
for filename in os.listdir(folder_path):
   if filename.endswith(('.jpg', '.png', '.jpeg')):  
    image_path = os.path.join(folder_path, filename)
    
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply template matching
    res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
    # Find the minimum and maximum values
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # Get the top-left corner of the matched region
    top_left = min_loc
    # Get the bottom-right corner of the matched region
    w, h = template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(top_left, bottom_right)
    # Draw a rectangle around the matched region
    cv2.rectangle(images, top_left, bottom_right, (255, 255, 0), 2)
    
# Show the results
cv2.imshow('Image with matched region', images)
cv2.imwrite(f'D:\TemplateMatching.png', images)
cv2.waitKey(0)
cv2.destroyAllWindows()  


# Apply template matching
# 

# # Find the minimum and maximum values
# 

# # Get the top-left corner of the matched region
# top_left = min_loc

# # Get the bottom-right corner of the matched region
# w, h = template.shape[::-1]
# bottom_right = (top_left[0] + w, top_left[1] + h)
# print(top_left, bottom_right)
# # Draw a rectangle around the matched region
# cv2.rectangle(images, top_left, bottom_right, (255, 255, 0), 2)

# # Show the results
# cv2.imshow('Image with matched region', images)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import numpy as np
from PIL import Image
import cv2

# Load the image using Pillow
image = Image.open('D:\workspace\DA Python XLA\Image\meo.jpg')

# Specify the rotation angle in radians (positive values for clockwise)
angle = np.radians(-45)

# Get the image dimensions
width, height = image.size

# Create an empty NumPy array for the rotated image
rotated_image = np.zeros((height, width, 3), dtype=np.uint8)

# Calculate the rotation matrix
cos_theta = np.cos(angle)
sin_theta = np.sin(angle)
center_x = width // 2
center_y = height // 2

# Perform the rotation manually using the rotation matrix
for y in range(height):
    for x in range(width):
        # Translate coordinates to center
        translated_x = x - center_x
        translated_y = y - center_y

        # Apply rotation
        new_x = int(translated_x * cos_theta - translated_y * sin_theta + center_x)
        new_y = int(translated_x * sin_theta + translated_y * cos_theta + center_y)

        # Check if the new coordinates are within bounds
        if 0 <= new_x < width and 0 <= new_y < height:
            rotated_image[y, x] = image.getpixel((new_x, new_y))

# Create a Pillow image from the rotated NumPy array
rotated_image = Image.fromarray(rotated_image)

# Display the original and rotated images
open_cv_image = np.array(rotated_image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy() 
cv2.imshow('cocailol',open_cv_image)
if cv2.waitKey(0) & 0xff ==27 :
    cv2.destroyAllWindows()


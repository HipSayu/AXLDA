import math
import numpy as np
from PIL import Image
img = Image.open('D:\workspace\DA Python XLA\Image\meo.jpg')
Im = np.array(img)

angle = 30
# Define the most occuring variables
angle=math.radians(angle)                               #converting degrees to radians
cosine=math.cos(angle)
sine=math.sin(angle)
height=Im.shape[0]                                   #define the height of the image
width=Im.shape[1]                                    #define the width of the image

# Define the height and width of the new image that is to be formed
new_height  = round(abs(Im.shape[0]*cosine)+abs(Im.shape[1]*sine))+1
new_width  = round(abs(Im.shape[1]*cosine)+abs(Im.shape[0]*sine))+1

# define another image variable of dimensions of new_height and new _column filled with zeros
Rot_Im=np.zeros((new_height,new_width,Im.shape[2]))

# Find the centre of the image about which we have to rotate the image
original_centre_height   = round(((Im.shape[0]+1)/2)-1)    #with respect to the original image
original_centre_width    = round(((Im.shape[1]+1)/2)-1)    #with respect to the original image

# Find the centre of the new image that will be obtained
new_centre_height= round((((new_height)+1)/2)-1)        #with respect to the new image
new_centre_width= round((((new_width)+1)/2)-1)          #with respect to the new image

for i in range(height):
    for j in range(width):
        #co-ordinates of pixel with respect to the centre of original image
        y0=Im.shape[0]-1-i-original_centre_height                   
        x0=Im.shape[1]-1-j-original_centre_width
                     

        #co-ordinate of pixel with respect to the rotated image
        new_y0=round(x0*sine+y0*cosine)
        new_x0=round(x0*cosine-y0*sine)

        '''since image will be rotated the centre will change too, 
           so to adust to that we will need to change new_x and new_y with respect to the new centre'''
        new_y0=new_centre_height-new_y0
        new_x0=new_centre_width-new_x0

        # adding if check to prevent any errors in the processing
        if 0 <= new_x0 < new_width and 0 <= new_y0 < new_height and new_x0>=0 and new_y0>=0:
            Rot_Im[new_y0,new_x0,:]=Im[i,j,:]                          #writing the pixels to the new destination in the output image

pil_img=Image.fromarray((Rot_Im).astype(np.uint8))                       # converting array to image
img.show()
pil_img.show()                                               # saving the image
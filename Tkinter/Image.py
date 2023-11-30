import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Function to open an image using OpenCV
def open_image():
    file_path = 'D:\workspace\DA Python XLA\Image\meo.jpg'
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)
            label.config(image=photo)
            label.image = photo
        else:
            label.config(text="Invalid image file")

# Create the main window
root = tk.Tk()
root.title("OpenCV and Tkinter")

# Create a label for displaying the image
label = tk.Label(root)
label.pack()

# Create an entry field for entering the image file path
entry = tk.Entry(root)
entry.pack()

# Create a button to open the image
button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

# Start the Tkinter main loop
root.mainloop()

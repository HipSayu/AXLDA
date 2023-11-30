from tkinter import *
import cv2
from PIL import Image, ImageTk
import time


class App :
    def __init__(self, video_source = 0 ) :
        self.appName = 'Detected face'
        self.window = Tk ()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        # self.window.wm_iconbitmap('../Image/camera.png')
        self.window['bg'] = 'blue'   
        self.video_source = video_source
        
        #Video
        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text = self.appName, font=15, 
                           bg='blue', fg='white').pack(side=TOP, fill=BOTH)
        #create a canvas that can fit above video source size
        self.canvas = Canvas(self.window, width= self.vid.width, height=self.vid.height, bg='red')
        self.canvas.pack()
        
        #Button that lets the user take a snapshot
        
        self.btn_snapShot = Button(self.window, text='SnapShot', width= 30, bg='goldenrod2',
                                   activebackground= 'red')
        self.btn_snapShot.pack(anchor=CENTER, expand=TRUE)
        self.update()
        self.window.mainloop()
        
    def update(self):
        # Get a frame from the video source
        isTrue, frame = self.vid.getFrame()
        
        if isTrue :
            self.photo = ImageTk.PhotoImage(image= Image.fromarray(frame))
            self.canvas.create_image(0, 0, image= self.photo, anchor=NW)
        self.window.after(15, self.update)



class MyVideoCapture :
    def __init__(self, video_source = 0 ):
        #OPEN the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError('Unable to open this camera \n select another video source', video_source)
        # GET video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue :
                # if isTrue is true then current frame converted to RGB
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else :
                return(isTrue, None)
        else :
             return(isTrue, None)
         
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class MyImage :
    def __init__(self, path_file ='' ):
        #OPEN the video source
        self.image = cv2.imread(path_file)
        if self.image != None :
           
            # GET imageeo source width and height
            self.width = self.image.shape[0]
            self.height = self.image.shape[1]
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            self.photo = ImageTk.PhotoImage(image=image)
            self.label.config(image=self.photo)
            self.label.image = self.photo
        else:
            self.label.config(text="Invalid image file")
            raise ValueError('Unable to open this camera \n select another imageeo source', path_file)
    

if __name__ == '__main__':
    App()
         
         

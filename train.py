
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.title('Train Data')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='#c2b2f0')


        self.bg1_image = Image.open('Image\\bg1.jpg')
        photo = ImageTk.PhotoImage(self.bg1_image)
        self.bg1_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg1_image_label.image = photo
        self.bg1_image_label.place(x=65,y=100)


        self.title_label = Label(self.root, text='TRAIN DATA SET ', bg ='#c2b2f0', fg='#203e4a', font=('Cooper Black', 30, 'bold','underline'))
        self.title_label.place(x=550,y=10)


        self.train_button = Image.open('Image\\train.jpg')
        photo = ImageTk.PhotoImage(self.train_button)
        self.train_button_label = Button(self.root, image=photo,bg ='#edf1fe',relief=RAISED, bd=3, activebackground="#edf1fe",cursor= 'hand2', command=self.train_classifier)
        self.train_button_label.image = photo
        self.train_button_label.place(x=550,y=170)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        #============== Train the classifier and save===========

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!",parent=self.root)

























if __name__ == '__main__':
    root = Tk()
    app = Train(root)
    root.mainloop()

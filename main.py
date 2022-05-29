
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from Student import Student
from train import Train
from detect import Face_detect
from attendance import attendance
import sqlite3
import os

class Face_Recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.title('Face Recognition System')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='white')
     
        

        self.Details_button = Button(self.root, text='Student Details',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe', command=self.student_details)
        self.Details_button.place(x=358,y=200)

        self.Detector_button = Button(self.root, text='Face Detectopr',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe', command=self.detect)
        self.Detector_button.place(x=358,y=300)

        self.Attendance_button = Button(self.root, text='Attendance',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe', command=self.attendance)
        self.Attendance_button.place(x=358,y=400)

        self.Train_data_button = Button(self.root, text='Train data',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe', command=self.train_details)
        self.Train_data_button.place(x=358,y=500)

        self.Photos_button = Button(self.root, text='Photos',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe',command=self.open_img)
        self.Photos_button.place(x=358,y=600)



    def open_img(self):
        os.startfile("data")





#=========================Function Button==============================


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def detect(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_detect(self.new_window)



    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)





   






if __name__ == '__main__':
    root = Tk()
    app = Face_Recognition_system(root)
    root.mainloop()



from tkinter import *
from xml.dom import minicompat
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import sys





class Face_detect:
    def __init__(self,root):
        self.root = root
        self.root.title('Face Detect')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='#c2b2f0')


        self.bg_image = Image.open('Image\\bg2.jpg')
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg_image_label.image = photo
        self.bg_image_label.place(x=65,y=100)


        self.title_label = Label(self.root, text='Face Recognition', bg ='#c2b2f0', fg='#203e4a', font=('Cooper Black', 30, 'bold','underline'))
        self.title_label.place(x=550,y=10)


        self.detect_button = Image.open('Image\\detect.jpg')
        photo = ImageTk.PhotoImage(self.detect_button)
        self.detect_button_label = Button(self.root, image=photo,bg ='#604494', relief= RAISED, activebackground="#604494",cursor= 'hand2', bd=4, command=self.face_detect)
        self.detect_button_label.image = photo
        self.detect_button_label.place(x=570,y=355)


        #================attendance==================

    def mark_attendance(self,r,n,d):
        with open("Admin.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1= now.strftime("%d/%m/%Y")
                dtString= now.strftime("%H.%M.%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")




        #================face recognition===============


    def face_detect(self):   
        face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cap=cv2.VideoCapture(0)
        
        while True:
            _, img = cap.read()
            recognizer=cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("classifier.xml")
            id=0
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cas.detectMultiScale(gray, 1.3, 7)
            coord=[]
            for(x,y,w,h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                id, predict = recognizer.predict(roi_gray)
                conf=int((100*(1-predict/300)))

                conn= sqlite3.connect("student.db")
                cur= conn.cursor()

                cur.execute("select name from details where roll="+str(id))
                n=cur.fetchone()
                n="+".join(n)

                cur.execute("select roll from details where roll="+str(id))
                r=cur.fetchone()
                r="+".join(r)

                cur.execute("select dept from details where roll="+str(id))
                d=cur.fetchone()
                d="+".join(d)

                if conf>77: 
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

         
              
                cv2.imshow('frame', img)

                return coord
                
            
            if cv2.waitKey(100) & 0xFF == ord('q'):
                 break;
            cap.release()
            cv2.destroyAllWindows()

               
        




if __name__ == '__main__':
    root = Tk()
    app = Face_detect(root)
    root.mainloop()


from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='#c2b2f0')


        #===================variables==================

          
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()



        self.bg_image = Image.open('Image\\bg.png')
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg_image_label.image = photo
        self.bg_image_label.place(x=680,y=490)

        
        self.student_label = Label(self.root, text='STUDENT DETAILS', bg ='#c2b2f0', fg='#203e4a', font=('Cooper Black', 30, 'bold','underline'))
        self.student_label.place(x=550,y=10)

        self.bg1_image = Image.open('Image\\bg1.png')
        photo = ImageTk.PhotoImage(self.bg1_image)
        self.bg1_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg1_image_label.image = photo
        self.bg1_image_label.place(x=80,y=90)

        
        self.side_image = Image.open('Image\\side.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.root, image=photo,bg ='#E3E6FF')
        self.side_image_label.image = photo
        self.side_image_label.place(x=345,y=100)

        #==============name=====================
        
        self.name_label = Label(self.root, text='Student Name : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.name_label.place(x=130,y=190)

        self.name_entry = Entry(self.root, textvariable=self.var_name, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.name_entry.place(x=290,y=193)

        self.name_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.name_line.place(x=290,y=215)


        #==================department===================


        self.dept_label = Label(self.root, text='Department : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.dept_label.place(x=130,y=240)

        self.dept_entry = Entry(self.root, textvariable=self.var_dept, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.dept_entry.place(x=290,y=243)

        self.dept_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.dept_line.place(x=290,y=265)


        #====================year=========================
        self.year_label = Label(self.root, text='Year : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.year_label.place(x=130,y=290)

        self.year_entry = Entry(self.root, textvariable=self.var_year, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.year_entry.place(x=290,y=293)

        self.year_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.year_line.place(x=290,y=315)


        #=====================semester====================


        self.sem_label = Label(self.root, text='Semester : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.sem_label.place(x=130,y=340)

        self.sem_entry = Entry(self.root, textvariable=self.var_sem, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.sem_entry.place(x=290,y=343)

        self.sem_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.sem_line.place(x=290,y=365)
        

        #=====================division====================


        self.div_label = Label(self.root, text='Section : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.div_label.place(x=130,y=390)

        self.div_entry = Entry(self.root, textvariable=self.var_sec, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.div_entry.place(x=290,y=393)

        self.div_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.div_line.place(x=290,y=415)


        #=======================roll=======================


        self.roll_label = Label(self.root, text='Roll No : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.roll_label.place(x=130,y=440)

        self.roll_entry = Entry(self.root, textvariable=self.var_roll, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.roll_entry.place(x=290,y=443)

        self.roll_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.roll_line.place(x=290,y=465)


        #======================email=======================


        self.email_label = Label(self.root, text='Email : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.email_label.place(x=130,y=490)

        self.email_entry = Entry(self.root, textvariable=self.var_email, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.email_entry.place(x=290,y=493)

        self.email_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.email_line.place(x=290,y=515)


        #======================phn no==================


        self.no_label = Label(self.root, text='Contact No : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.no_label.place(x=130,y=540)

        self.no_entry = Entry(self.root, textvariable=self.var_no, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.no_entry.place(x=290,y=543)

        self.no_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.no_line.place(x=290,y=565)

       
        #=======================gender====================


        self.gender_label = Label(self.root, text='Gender : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.gender_label.place(x=130,y=590)

        self.gender_entry = Entry(self.root, textvariable=self.var_gender, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.gender_entry.place(x=290,y=593)

        self.gender_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.gender_line.place(x=290,y=615)

        
        #=======================DOB=======================


        self.dob_label = Label(self.root, text='Date of Birth : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.dob_label.place(x=130,y=640)

        self.dob_entry = Entry(self.root, textvariable= self.var_dob, highlightthickness=0, relief=FLAT, width=39, bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13 ))
        self.dob_entry.place(x=290,y=643)

        self.dob_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.dob_line.place(x=290,y=665)


        #====================photo button======================


        self.button= Button(self.root, text='Save',  width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'), command= self.add_data)
        self.button.place(x=138,y=700)

        self.button= Button(self.root, text='Update', width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.update_data)
        self.button.place(x=268,y=700)

        self.button= Button(self.root, text='Delete', width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.delete_data)
        self.button.place(x=398,y=700)

        self.button= Button(self.root, text='Reset', width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.reset_data)
        self.button.place(x=528,y=700)

        self.button= Button(self.root, text='Take Photo Sample', width=15, bd=1, relief= GROOVE, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.generate_dataset)
        self.button.place(x=300,y=760)


         #=========================Right Side========================



        self.right_image = Image.open('Image\\right.png')
        photo = ImageTk.PhotoImage(self.right_image)
        self.right_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.right_image_label.image = photo
        self.right_image_label.place(x=700,y=90)


        self.search_label= Label(self.root, text='Search By: ', bg='#E3E6FF', fg='#464196', font=('Times New Roman', 13,'bold' ))
        self.search_label.place(x=800,y=130)

        self.search_entry = ttk.Combobox(self.root, width=24, font=('Times New Roman', 11 ))
        self.search_entry['values']=('Student name','Roll No',"Year","Semester","Department")
        self.search_entry['state'] = 'readonly'
        self.search_entry.place(x=900,y=133)
        self.search_entry.current(0)

        self.search_button= Button(self.root, text='Search', width=8, bd=3, relief=RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 11,'bold'))
        self.search_button.place(x=1150,y=125)

        self.show_button= Button(self.root, text='Show All', width=8, bd=3, relief=RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 11,'bold'))
        self.show_button.place(x=1300,y=125)

        
        self.table_frame=Frame(self.root,bg='#E3E6FF',relief=GROOVE, bd=4)
        self.table_frame.place(x=730,y=180,width=710,height=300)
        
        self.scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=ttk.Scrollbar(self.table_frame,orient=VERTICAL)

        self.table=ttk.Treeview(self.table_frame,column=('Name','Department','Year','Semester','Section','Roll','Email','Contact No','Gender','DOB'),xscrollcommand=self.scroll_x.set ,yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)


        self.table.heading('Name',text="Name")
        self.table.heading('Department',text="Department")
        self.table.heading('Year',text="Year")
        self.table.heading('Semester',text="Semester")
        self.table.heading('Section',text="Section")
        self.table.heading('Roll',text="Roll")
        self.table.heading('Email',text="Email")
        self.table.heading('Contact No',text="Contact No")
        self.table.heading('Gender',text="Gender")
        self.table.heading('DOB',text="DOB")
        self.table['show']='headings'

        self.table.column('Name',width=100)
        self.table.column('Department',width=100)
        self.table.column('Year',width=100)
        self.table.column('Semester',width=100)
        self.table.column('Section',width=100)
        self.table.column('Roll',width=100) 
        self.table.column('Email',width=100)
        self.table.column('Contact No',width=100)
        self.table.column('Gender',width=100)
        self.table.column('DOB',width=100)
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


#========================Function Declaration=======================

    
    def add_data(self):
        if self.var_name.get()=='' or self.var_dept.get()=='' or self.var_year.get()=='' or self.var_sem.get()=='' or self.var_sec.get()=='' or self.var_roll.get()=='' or self.var_email.get()=='' or self.var_no.get()=='' or self.var_gender.get()=='' or self.var_dob.get()=='':
            messagebox.showerror('Error','All fields are required', parent=self.root)
        else:
            conn= sqlite3.connect("student.db")
            cur= conn.cursor()
            try:
                cur.execute("INSERT INTO details (name,dept,year,sem,sec,roll,email,no,gender,dob) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                    self.var_name.get(),
                    self.var_dept.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_sec.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Student details has been added Successfully',parent=self.root)
            except:
                messagebox.showerror('Error','Student roll no already exists.',parent=self.root)
            

#================fetch data===================


    def fetch_data(self):
        conn= sqlite3.connect("student.db")
        cur= conn.cursor()
        cur.execute('select * from details')
        data= cur.fetchall()
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert('',END,values=i)
            conn.commit()
        conn.close()

            

#=================get cursor=================


    def get_cursor(self,event=""):
        cursor_focus=self.table.focus()
        content=self.table.item(cursor_focus)
        data= content['values']
        self.var_name.set(data[0]),
        self.var_dept.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_sec.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_email.set(data[6]),
        self.var_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9])


#===================update function=====================

    
    def update_data(self):
        if self.var_name.get()=='' or self.var_dept.get()=='' or self.var_year.get()=='' or self.var_sem.get()=='' or self.var_sec.get()=='' or self.var_roll.get()=='' or self.var_email.get()=='' or self.var_no.get()=='' or self.var_gender.get()=='' or self.var_dob.get()=='':
            messagebox.showerror('Error','All fields are required', parent=self.root)
        else:
            Update=messagebox.askyesno('Update','Do you want to update this student details?', parent=self.root)
            if Update>0:
                conn= sqlite3.connect("student.db")
                cur= conn.cursor()  
                cur.execute("select * from details where roll=?",(self.roll_entry.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","If you want to update roll then delete current details and add new details",parent=self.root)
                else:
                    cur.execute('update details set name=?,dept=?,year=?,sem=?,sec=?,email=?,no=?,gender=?,dob=? where roll=?',(
                        self.name_entry.get(),
                        self.dept_entry.get(),
                        self.year_entry.get(),
                        self.sem_entry.get(),
                        self.div_entry.get(),
                        self.email_entry.get(),
                        self.no_entry.get(),
                        self.gender_entry.get(),
                        self.dob_entry.get(),
                        self.roll_entry.get(),))
            else:
                if not Update:
                    return
            conn.commit()
            messagebox.showinfo('Success','Student details has been updated successfully',parent=self.root)
            self.fetch_data()
            conn.close()
            


#===================delete function=====================

    
    def delete_data(self):
        delete=messagebox.askyesno('Delete','Do you want to delete this student details?',parent=self.root)
        if delete>0:
            conn= sqlite3.connect("student.db")
            cur= conn.cursor()
            cur.execute("delete from details where roll=?",(self.roll_entry.get(),))
        else:
            if not delete:
                return
        conn.commit()
        messagebox.showinfo('Success','Student details has been deleted successfully',parent=self.root)
        self.fetch_data()
        conn.close()
        
  
#===================Reset function=====================

    
    def reset_data(self): 
        self.var_name.set(''),
        self.var_dept.set(''),
        self.var_year.set(''),
        self.var_sem.set(''),
        self.var_sec.set(''),
        self.var_roll.set(''),
        self.var_email.set(''),
        self.var_no.set(''),
        self.var_gender.set(''),
        self.var_dob.set('')
        

#======================Generate data set or take photo sample=====================

    def generate_dataset(self):
        if self.var_name.get()=='' or self.var_dept.get()=='' or self.var_year.get()=='' or self.var_sem.get()=='' or self.var_sec.get()=='' or self.var_roll.get()=='' or self.var_email.get()=='' or self.var_no.get()=='' or self.var_gender.get()=='' or self.var_dob.get()=='':
            messagebox.showerror('Error','All fields are required', parent=self.root)
        else:
            conn= sqlite3.connect("student.db")
            cur= conn.cursor()  
            cur.execute("select * from details where roll=?",(self.roll_entry.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","If you want to update roll then delete current details and add new details",parent=self.root)
            else:
                vid_cam=cv2.VideoCapture(0)
                face_detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                count=0
                while(True):
                    _, image_frame = vid_cam.read() 
                    gray=cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
                    faces= face_detector.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h)in faces:
                        cv2.rectangle(image_frame,(x,y),(x+w,y+h),(255,0,0),2)
                        count+=1
                        cv2.imwrite("data/User."+ str(self.var_roll.get())+'.'+str(count)+".png",gray[y:y+h,x:x+w])
                        cv2.imshow('frame',image_frame)
                    if cv2.waitKey(1)==13 or int(count)==100:
                       print("Successfully Captured")
                       break
                vid_cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result','Generating data sets completed!',parent=self.root)




           




if __name__ == '__main__':
    root = Tk()
    app = Student(root)
    root.mainloop()


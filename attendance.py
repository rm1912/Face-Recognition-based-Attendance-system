from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class attendance:
    def __init__(self,root):
        self.root = root
        self.root.title('Attendace Record')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='#c2b2f0')


        #===================variables==================

          
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_roll=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attendance=StringVar()



        self.bg_image = Image.open('Image\\bg3.png')
        photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg_image_label.image = photo
        self.bg_image_label.place(x=1000,y=490)

        
        self.student_label = Label(self.root, text='STUDENT ATTENDANCE', bg ='#c2b2f0', fg='#203e4a', font=('Cooper Black', 30, 'bold','underline'))
        self.student_label.place(x=550,y=10)

        self.bg1_image = Image.open('Image\\bg1.png')
        photo = ImageTk.PhotoImage(self.bg1_image)
        self.bg1_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.bg1_image_label.image = photo
        self.bg1_image_label.place(x=80,y=90)

        
        self.side_image = Image.open('Image\\right.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.root, image=photo,bg ='#c2b2f0')
        self.side_image_label.image = photo
        self.side_image_label.place(x=700,y=90)

        #==============name=====================
        
        self.name_label = Label(self.root, text='Student Name : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.name_label.place(x=130,y=190)

        self.name_entry = Entry(self.root, textvariable=self.var_name, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='#5c6274', font=('Times New Roman', 13 ))
        self.name_entry.place(x=290,y=193)

        self.name_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.name_line.place(x=290,y=215)


        #==================department===================


        self.dept_label = Label(self.root, text='Department : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.dept_label.place(x=130,y=240)

        self.dept_entry = Entry(self.root, textvariable=self.var_dept, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='#5c6274', font=('Times New Roman', 13 ))
        self.dept_entry.place(x=290,y=243)

        self.dept_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.dept_line.place(x=290,y=265)


        #====================roll=========================


        self.roll_label = Label(self.root, text='Roll No : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.roll_label.place(x=130,y=290)

        self.roll_entry = Entry(self.root, textvariable=self.var_roll, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='#5c6274', font=('Times New Roman', 13 ))
        self.roll_entry.place(x=290,y=293)

        self.roll_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.roll_line.place(x=290,y=315)


        #=====================time====================


        self.time_label = Label(self.root, text='Time : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.time_label.place(x=130,y=340)

        self.time_entry = Entry(self.root, textvariable=self.var_time, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='#5c6274', font=('Times New Roman', 13 ))
        self.time_entry.place(x=290,y=343)

        self.time_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.time_line.place(x=290,y=365)
        

        #=====================date====================


        self.date_label = Label(self.root, text='Date : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.date_label.place(x=130,y=390)

        self.date_entry = Entry(self.root, textvariable=self.var_date, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='#5c6274', font=('Times New Roman', 13 ))
        self.date_entry.place(x=290,y=393)

        self.date_line = Canvas(self.root, width=355, height=2, bg='#5c6274', highlightthickness=0)
        self.date_line.place(x=290,y=415)


        #======================attendance=======================


        self.status_label = Label(self.root, text='Attendance Status : ',bg='#E3E6FF', fg='#464196', font=('Times New Roman', 15,'bold' ))
        self.status_label.place(x=130,y=440)

        self.status_entry = ttk.Combobox(self.root, width=40, textvariable=self.var_attendance, font=('Arial', 11 ))
        self.status_entry['values']=('Select','Present','Absent')
        self.status_entry['state'] = 'readonly'
        self.status_entry.place(x=305,y=442)
        self.status_entry.current(0)

        self.status_line = Canvas(self.root, width=343, height=2, bg='#5c6274', highlightthickness=0)
        self.status_line.place(x=306,y=465)



        #======================right side======================


        self.table_frame=Frame(self.root,bg='#E3E6FF',relief=GROOVE, bd=4)
        self.table_frame.place(x=730,y=110,width=710,height=355)
        
        self.scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=ttk.Scrollbar(self.table_frame,orient=VERTICAL)

        self.table=ttk.Treeview(self.table_frame,column=('Roll','Name','Department','Date','Time','Attendance'),xscrollcommand=self.scroll_x.set ,yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)


        self.table.heading('Roll',text="Roll")
        self.table.heading('Name',text="Name")
        self.table.heading('Department',text="Department")
        self.table.heading('Date',text="Date")
        self.table.heading('Time',text="Time")
        self.table.heading('Attendance',text="Attendance")
        self.table['show']='headings'

        self.table.column('Roll',width=100)
        self.table.column('Name',width=100)
        self.table.column('Department',width=100)
        self.table.column('Date',width=100)
        self.table.column('Time',width=100)
        self.table.column('Attendance',width=100)
        self.table.pack(fill=BOTH,expand=1)

        self.table.bind("<ButtonRelease>",self.get_cursor)


        #=======================button======================


        self.button= Button(self.root, text='Import csv',  width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.importCsv)
        self.button.place(x=138,y=700)

        self.button= Button(self.root, text='Export csv', width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'),command=self.exportCsv)
        self.button.place(x=330,y=700)

        self.button= Button(self.root, text='Reset', width=10, bd=3, relief= RAISED, highlightthickness=0, cursor= 'hand2', bg='#EEF3FF', fg='#5c6274', font=('Times New Roman', 13,'bold'), command=self.reset_data)
        self.button.place(x=528,y=700)


        #==================fetch data==================

    def fetchData(self,rows):
        self.table.delete(*self.table.get_children())
        for i in rows:
            self.table.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for r in csvread:
                mydata.append(r)
            self.fetchData(mydata)


    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for r in mydata:
                    exp_write.writerow(r)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully",parent=self.root)
        except:
                messagebox.showerror('Error','Error!',parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        data= content['values']
        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dept.set(data[2]),
        self.var_date.set(data[3]),
        self.var_time.set(data[4]),
        self.var_attendance.set(data[5])



    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set(""),
        self.var_dept.set(""),
        self.var_date.set(""),
        self.var_time.set(""),
        self.var_attendance.set("")
        

if __name__ == '__main__':
    root = Tk()
    app = attendance(root)
    root.mainloop()

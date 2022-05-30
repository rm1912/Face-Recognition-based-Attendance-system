from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from main import Face_Recognition_system
import sqlite3
 

class LoginForm:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1000x500')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.configure(bg='#736a86')

        self.frame= Frame(self.root,width=1245,height=650,bg='#edf1fe')
        self.frame.place(x=150,y=100)

        self.frame= Frame(self.root,width=621,height=650,bg='#b73275')
        self.frame.place(x=774,y=100)

        #==============Heading================
       
        self.heading = Label(self.root, text='WELCOME', font=('Forte', 40, 'bold'), bg='#edf1fe', fg='#464196')
        self.heading.place(x=340, y=150)

        #==============Right side upper image================

        self.side_image = Image.open('Image\\bgg.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.root, image=photo,bg ='#b73275')
        self.side_image_label.image = photo
        self.side_image_label.place(x=888,y=100)

        #===============Right side lower image=================

        self.side_image2 = Image.open('Image\\bg2.png')
        photo = ImageTk.PhotoImage(self.side_image2)
        self.side_image2_label = Label(self.root, image=photo,bg ='#b73275')
        self.side_image2_label.image = photo
        self.side_image2_label.place(x=920,y=420)

        #==============Sign in Image====================

        self.sign_image = Image.open('Image\\hi.png')
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_image_label = Label(self.root, image=photo,bg ='#edf1fe')
        self.sign_image_label.image = photo
        self.sign_image_label.place(x=410,y=260)


        self.sign_in_label = Label(self.root, text='Sign In',bg='#edf1fe', fg='#464196', font=('Cooper Black', 23, 'bold'))
        self.sign_in_label.place(x=403,y=380)

        #================username=====================

        self.user_label = Label(self.root, text='Email',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 15 ))
        self.user_label.place(x=283,y=460)

        self.user_entry = Entry(self.root, highlightthickness=0, relief=FLAT, width=30, bg='#dae4ee', fg='#8b95a2', font=('Yu Gothic UI Semibold', 13 ))
        self.user_entry.place(x=385,y=460)

        self.user_line = Canvas(self.root, width=273, height=2, bg='black', highlightthickness=0)
        self.user_line.place(x=385,y=485)

        #================password======================

        self.password_label = Label(self.root, text='Password',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 15 ))
        self.password_label.place(x=285,y=530)

        self.password_entry = Entry(self.root, highlightthickness=0, relief=FLAT, width=30, bg='#dae4ee', fg='#8b95a2', font=('Yu Gothic UI Semibold', 13 ))
        self.password_entry.place(x=385,y=530)

        self.password_line = Canvas(self.root, width=273, height=2, bg='black', highlightthickness=0)
        self.password_line.place(x=385,y=555)

        #===============Login Button================

        
        self.lgn_button = Image.open('Image\\login.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Button(self.root, image=photo,bg ='#edf1fe',activebackground="#edf1fe",cursor= 'hand2', bd=0, command=self.login)
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=400,y=580)


        #==============Forgot password==============

        self.forgot_button = Button(self.root, text='Forgot Password ?',fg='#464197', font=('Yu Gothic UI Semibold', 12, 'underline' ),width=25,bd=0, bg='#edf1fe', cursor='hand2', activebackground='#edf1fe', command=self.Reset_password_window)
        self.forgot_button.place(x=358,y=627)

        #==============Sign up===============

        self.sign_label= Label(self.root, text='No account yet?', font=('Yu Gothic UI Semibold', 13, 'bold'), background='#edf1fe',fg='#739bd0')
        self.sign_label.place(x=338,y=685)

        self.signup_button = Image.open('Image\\signup1.png')
        photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Button(self.root, image=photo,bg ='#edf1fe', activebackground="#edf1fe", cursor= 'hand2', bd=0, command=self.register_window)
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=470,y=680)

        #==============Show/Hide Password==============

        self.show_image = Image.open('Image\\show.jpg')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
       
       
        self.hide_image = Image.open('Image\\hide.jpg')
        self.photo = ImageTk.PhotoImage(self.hide_image)
        self.hide_button = Button(self.root, image=self.photo,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=630,y=532)


    def show(self):
        self.hide_button = Button(self.root, image=self.photo,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=630,y=532)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.root, image=self.photo1,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=630,y=532)
        self.password_entry.config(show='*')

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.user_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror('Error','All  fields are required')

        else:
            conn= sqlite3.connect('database.db')
            cur= conn.cursor() 
            cur.execute("select * from users where email=? and password=?",(self.user_entry.get(), self.password_entry.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_system(self.new_window)

            conn.commit()
            conn.close()



    def reset_pass(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error","Please enter email address",parent=self.root2)
        elif self.Question_entry.get()=="Select":
            messagebox.showerror("Error","Please select security question",parent=self.root2)
        elif self.Answer_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.password_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn= sqlite3.connect('database.db')
            cur= conn.cursor() 
            cur.execute("select * from users where email=? and Question=? and Answer=?",(self.email_entry.get(), self.Question_entry.get(), self.Answer_entry.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct details",parent=self.root2)
            else:
                cur.execute("update users set password=? where email=?",(self.password_entry.get(),self.email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your passowrd has been reset , Please login with new password",parent=self.root2)
                self.root2.destroy()










    #======================Reset Password======================


    def Reset_password_window(self):
        self.root2=Toplevel()
        self.root2.title('Reset Password')
        self.root2.geometry('1000x500')
        self.root2.state('zoomed')
        self.root2.resizable(0,0)
        self.root2.configure(bg='#736a86')

        self.frame1= Frame(self.root2,width=612,height=547,bg='#edf1fe')
        self.frame1.place(x=190,y=100)


        #==============Heading================
       
        self.heading = Label(self.root2, text='Reset Password', font=('Forte', 30), bg='#edf1fe', fg='#464196')
        self.heading.place(x=320, y=140)

        self.side_image = Image.open('Image\\pass.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.root2, image=photo,bg ='#edf1fe')
        self.side_image_label.image = photo
        self.side_image_label.place(x=740,y=100)

        #=====================email address==================


        self.email_label = Label(self.root2, text='Email Address : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.email_label.place(x=245,y=250)

        self.email_entry = Entry(self.root2, highlightthickness=0, relief=FLAT, width=36, bg='white', fg='black', font=('Arial', 11 ))
        self.email_entry.place(x=370,y=253)

        self.email_line = Canvas(self.root2, width=292, height=2, bg='black', highlightthickness=0)
        self.email_line.place(x=370,y=275)

        
        #=====================Question===================


        self.Question_label = Label(self.root2, text='Select Security Question : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.Question_label.place(x=245,y=330)

        self.Question_entry = ttk.Combobox(self.root2, width=24, font=('Arial', 11 ))
        self.Question_entry['values']=('Select','Your birth place',"Your pet's name","Your best friend's name","Your hobby")
        self.Question_entry['state'] = 'readonly'
        self.Question_entry.place(x=449,y=333)
        self.Question_entry.current(0)

        self.Question_line = Canvas(self.root2, width=212, height=2, bg='black', highlightthickness=0)
        self.Question_line.place(x=451,y=355)

       
       #=====================Answer=====================
       

        self.Answer_label = Label(self.root2, text='Security Answer : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.Answer_label.place(x=244,y=410)

        self.Answer_entry = Entry(self.root2, highlightthickness=0, relief=FLAT, width=34, bg='white', fg='black', font=('Arial', 11 ))
        self.Answer_entry.place(x=389,y=413)

        self.Answer_line = Canvas(self.root2, width=274, height=2, bg='black', highlightthickness=0)
        self.Answer_line.place(x=389,y=435)
     
        
        #===================password===================


        self.password_label = Label(self.root2, text='New Password : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.password_label.place(x=245,y=490)

        self.password_entry = Entry(self.root2, highlightthickness=0, relief=FLAT, width=35, bg='white', fg='black', font=('Arial', 11 ))
        self.password_entry.place(x=380,y=493)

        self.password_line = Canvas(self.root2, width=285, height=2, bg='black', highlightthickness=0)
        self.password_line.place(x=380,y=515)


        #==================Reset Button================


        self.reset_button = Image.open('Image\\reset.png')
        photo = ImageTk.PhotoImage(self.reset_button)
        self.reset_button_label = Button(self.root2, image=photo,bg ='#edf1fe',activebackground="#edf1fe",cursor= 'hand2', bd=0,command=self.reset_pass)
        self.reset_button_label.image = photo
        self.reset_button_label.place(x=400,y=550)


    







class Register:
    def __init__(self,root1):
        self.root1 = root1
        self.root1.title('Register')
        self.root1.geometry('1000x500')
        self.root1.state('zoomed')
        self.root1.resizable(0,0)
        self.root1.configure(bg='#736a86')

        self.frame= Frame(self.root1,width=621,height=650,bg='#edf1fe')
        self.frame.place(x=150,y=100)


        self.frame= Frame(self.root1,width=621,height=650,bg='#b73275')
        self.frame.place(x=771,y=100)


        #=============variables===============


        self.var_First_name=StringVar()
        self.var_Last_name=StringVar()
        self.var_no=StringVar()
        self.var_email=StringVar()
        self.var_Question=StringVar()
        self.var_Answer=StringVar()
        self.var_password=StringVar()
        self.var_confirm=StringVar()

     
        #============Right side image============

        
        self.side_image = Image.open('Image\\left.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.root1, image=photo,bg ='#b73275')
        self.side_image_label.image = photo
        self.side_image_label.place(x=830,y=120)


        self.note = Label(self.root1, text='Start your journey with us', font=('Forte', 30), bg='#b73275', fg='#edf1fe')
        self.note.place(x=860, y=650)


        #=============left side=============


        self.sign_image = Image.open('Image\\hi.png')
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_image_label = Label(self.root1, image=photo,bg ='#edf1fe')
        self.sign_image_label.image = photo
        self.sign_image_label.place(x=400,y=120)


        self.sign_up_label = Label(self.root1, text='Sign Up',bg='#edf1fe', fg='#464196', font=('Cooper Black', 23, 'bold'))
        self.sign_up_label.place(x=380,y=215)


        #================first name=====================

        self.First_name_label = Label(self.root1, text='First Name : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.First_name_label.place(x=245,y=280)

        self.First_name_entry = Entry(self.root1,textvariable=self.var_First_name, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='black', font=('Arial', 11 ))
        self.First_name_entry.place(x=345,y=283)

        self.First_name_line = Canvas(self.root1, width=318, height=2, bg='black', highlightthickness=0)
        self.First_name_line.place(x=345,y=305)


        #==================last name==================


        self.Last_name_label = Label(self.root1, text='Last Name : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.Last_name_label.place(x=245,y=330)

        self.Last_name_entry = Entry(self.root1, textvariable=self.var_Last_name, highlightthickness=0, relief=FLAT, width=39, bg='white', fg='black', font=('Arial', 11 ))
        self.Last_name_entry.place(x=345,y=333)

        self.Last_name_line = Canvas(self.root1, width=318, height=2, bg='black', highlightthickness=0)
        self.Last_name_line.place(x=345,y=355)

        
        #===================contact no=====================


        self.no_label = Label(self.root1, text='Contact No : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.no_label.place(x=245,y=380)

        self.no_entry = Entry(self.root1, textvariable=self.var_no, highlightthickness=0, relief=FLAT, width=38, bg='white', fg='black', font=('Arial', 11 ))
        self.no_entry.place(x=352,y=383)

        self.no_line = Canvas(self.root1, width=310, height=2, bg='black', highlightthickness=0)
        self.no_line.place(x=352,y=405)


        #=====================email address==================


        self.email_label = Label(self.root1, text='Email Address : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.email_label.place(x=245,y=430)

        self.email_entry = Entry(self.root1, textvariable=self.var_email, highlightthickness=0, relief=FLAT, width=36, bg='white', fg='black', font=('Arial', 11 ))
        self.email_entry.place(x=370,y=433)
        
        self.email_line = Canvas(self.root1, width=292, height=2, bg='black', highlightthickness=0)
        self.email_line.place(x=370,y=455)

        
        #=====================Question===================


        self.Question_label = Label(self.root1, text='Select Security Question : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.Question_label.place(x=245,y=480)



        self.Question_entry = ttk.Combobox(self.root1, textvariable=self.var_Question, width=24, font=('Arial', 11 ))
        self.Question_entry['values']=('Select','Your birth place',"Your pet's name","Your best friend's name","Your hobby")
        self.Question_entry['state'] = 'readonly'
        self.Question_entry.place(x=449,y=483)
        self.Question_entry.current(0)

        self.Question_line = Canvas(self.root1, width=212, height=2, bg='black', highlightthickness=0)
        self.Question_line.place(x=451,y=505)

       
       #=====================Answer=====================
       

        self.Answer_label = Label(self.root1, text='Security Answer : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.Answer_label.place(x=244,y=530)

        self.Answer_entry = Entry(self.root1, textvariable=self.var_Answer, highlightthickness=0, relief=FLAT, width=34, bg='white', fg='black', font=('Arial', 11 ))
        self.Answer_entry.place(x=389,y=533)

        self.Answer_line = Canvas(self.root1, width=274, height=2, bg='black', highlightthickness=0)
        self.Answer_line.place(x=389,y=555)
     
        
        #===================password===================


        self.password_label = Label(self.root1, text='Password : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.password_label.place(x=245,y=580)

        self.password_entry = Entry(self.root1, textvariable=self.var_password, highlightthickness=0, relief=FLAT, width=40, bg='white', fg='black', font=('Arial', 11 ))
        self.password_entry.place(x=335,y=583)

        self.password_line = Canvas(self.root1, width=328, height=2, bg='black', highlightthickness=0)
        self.password_line.place(x=335,y=605)


        #==================confirm password==================


        self.confirm_label = Label(self.root1, text='Confirm Password : ',bg='#edf1fe', fg='#739bd0', font=('Yu Gothic UI Semibold', 13 ))
        self.confirm_label.place(x=245,y=630)

        self.confirm_entry = Entry(self.root1, textvariable=self.var_confirm, highlightthickness=0, relief=FLAT, width=33, bg='white', fg='black', font=('Arial', 11 ))
        self.confirm_entry.place(x=400,y=633)
        
        self.confirm_line = Canvas(self.root1, width=263, height=2, bg='black', highlightthickness=0)
        self.confirm_line.place(x=400,y=655)


        #==================Register Button=================

        
        self.signup_button = Image.open('Image\\signup.png')
        photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Button(self.root1, image=photo, command= self.register_data, bg ='#edf1fe', activebackground="#edf1fe", cursor= 'hand2', bd=0)
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=380,y=680)


        #==================show/hide password==================


        self.show1_image = Image.open('Image\\show.jpg')
        self.photo1 = ImageTk.PhotoImage(self.show1_image)
       
       
        self.hide1_image = Image.open('Image\\hide.jpg')
        self.photo = ImageTk.PhotoImage(self.hide1_image)
        self.hide1_button = Button(self.root1, image=self.photo,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide1)
        self.hide1_button.image = self.photo
        self.hide1_button.place(x=630,y=580)


        self.show2_image = Image.open('Image\\show.jpg')
        self.photo2 = ImageTk.PhotoImage(self.show2_image)
       
       
        self.hide2_image = Image.open('Image\\hide.jpg')
        self.photo3 = ImageTk.PhotoImage(self.hide2_image)
        self.hide2_button = Button(self.root1, image=self.photo3,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide2)
        self.hide2_button.image = self.photo3
        self.hide2_button.place(x=630,y=630)


       

    
        
        
        
        
    def show1(self):
        self.hide1_button = Button(self.root1, image=self.photo,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide1)
        self.hide1_button.image = self.photo
        self.hide1_button.place(x=630,y=580)
        self.password_entry.config(show='')

    def hide1(self):
        self.show1_button = Button(self.root1, image=self.photo1,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.show1)
        self.show1_button.image = self.photo1
        self.show1_button.place(x=630,y=580)
        self.password_entry.config(show='*')


    def show2(self):
        self.hide2_button = Button(self.root1, image=self.photo3,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.hide2)
        self.hide2_button.image = self.photo3
        self.hide2_button.place(x=630,y=630)
        self.confirm_entry.config(show='')

    def hide2(self):
        self.show2_button = Button(self.root1, image=self.photo2,bg ='#dae4ee', activebackground="#dae4ee", cursor= 'hand2', bd=0, command=self.show2)
        self.show2_button.image = self.photo2
        self.show2_button.place(x=630,y=630)
        self.confirm_entry.config(show='*')






      #================Function declaration==================

    def register_data(self):
        if self.var_First_name.get()=="" or self.var_Last_name.get()=="" or self.var_no.get()=="" or self.var_email.get()=="" or self.var_Question.get()=="Select" or self.var_Answer.get()=="" or self.var_password.get()=="" or self.var_confirm.get()=="":
            messagebox.showerror('Error','All fields are required',parent=self.root1)
        elif self.var_password.get()!=self.var_confirm.get():
            messagebox.showerror('Error','Password and Confirm Password must be same',parent=self.root1)
        else:
            conn= sqlite3.connect('database.db')
            cur= conn.cursor()
            try:
                cur.execute("INSERT INTO users (First_name,Last_name,no,email,Question,Answer,password) VALUES (?, ?, ?, ?, ?, ?, ?)",(
                    self.var_First_name.get(),
                    self.var_Last_name.get(),
                    self.var_no.get(),
                    self.var_email.get(),
                    self.var_Question.get(),
                    self.var_Answer.get(),
                    self.var_password.get()
                ))
                conn.commit()
                messagebox.showinfo('Success','Registered Successfully',parent=self.root1)
                conn.close()
            except:
                messagebox.showerror('Error','User already exist,please try another email',parent=self.root1)



    def Face_Recognition_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_system(self.new_window)

            



def page():
    root = Tk()
    LoginForm(root)
    root.mainloop()

if __name__ == '__main__':
    page()

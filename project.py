from tkinter import *
import customtkinter as ct
from PIL import Image
import mysql.connector as mysql
import re

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')

# Welcome Page
root=ct.CTk()
root.geometry("540x450")
root.title("PES International Bank")




 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 

   

cnx=mysql.connect(user='root',password='Rogue@05',host='localhost')

if cnx.is_connected():
       print('connected')
       cur=cnx.cursor()
       cur.execute('create database if not exists project;')
       cur.execute('use project;')
       q1="create table if not exists details(slno int NOT NULL AUTO_INCREMENT PRIMARY KEY,NAME varchar(50) NOT NULL,AGE int NOT NULL,Gender varchar(2),Phone_no int(15),EMAIL varchar(50),password varchar(10) NOT NULL,BALANCE int Default 1000);"
       cur.execute(q1)

       def login():
              login_Screen=Toplevel(root)
              login_Screen.title("login")
              login_Screen.geometry("1000x500")
              login_Screen.configure(background='#252525')

              global temp_slno
              temp_slno = StringVar()
              global temp_password
              temp_password = StringVar()
              
              l1=ct.CTkLabel(login_Screen,text=" ** Enter Your details here ** ",font=('Portico Diagonal',26),text_color='white')
              l1.place(x=50)
              l2=ct.CTkLabel(login_Screen,text=" Account Number ",font=('Portico Diagonal',22),text_color='white')
              l2.place(x=50,y=50)
              l3=ct.CTkLabel(login_Screen,text=" password ",font=('Portico Diagonal',22),text_color='white')
              l3.place(x=50,y=100)
              e1=ct.CTkEntry(login_Screen,textvariable=temp_slno)
              e1.place(x=300,y=50)
              e2=ct.CTkEntry(login_Screen,textvariable=temp_password)
              e2.place(x=300,y=100)
              b1=ct.CTkButton(login_Screen,text="Login",font=('Portico Diagonal',20))
              b1.place(x=300,y=150)
              b2=ct.CTkButton(login_Screen,text="Forgot password",font=('Portico Diagonal',20))
              b2.place(x=50,y=150)

       
       def registration():
              Register_screen=Toplevel(root)
              Register_screen.title("Registration")
              Register_screen.geometry("1000x1000")
              Register_screen.configure(background='#252525')
       
        
              global notif1
              notif1=ct.CTkLabel(Register_screen,text="",font=('Portico Rounded',36),text_color='white')
              notif1.place(x=50,y=400)
              l1=ct.CTkLabel(Register_screen,text=" ** Enter Your details here ** ",font=('Portico Diagonal',26),text_color='white')
              l1.place(x=40,y=50)
              l2=ct.CTkLabel(Register_screen,text="Name  ",font=('Portico Diagonal',22),text_color='white')
              l2.place(x=50,y=100)
              l3=ct.CTkLabel(Register_screen,text="Age  ",font=('Portico Diagonal',22),text_color='white')
              l3.place(x=50,y=150)
              l4=ct.CTkLabel(Register_screen,text="Gender(M/F)  ",font=('Portico Diagonal',22),text_color='white')
              l4.place(x=50,y=200)
              l5=ct.CTkLabel(Register_screen,text="Password ",font=('Portico Diagonal',22),text_color='white')
              l5.place(x=50,y=250)
              l6=ct.CTkLabel(Register_screen,text="Email  ",font=('Portico Diagonal',22),text_color='white')
              l6.place(x=50,y=300)
              l7=ct.CTkLabel(Register_screen,text='Phone Number  ',font=('Portico Diagonal',22),text_color='white')
              l7.place(x=50,y=350)

              global temp_name
              global temp_age
              global temp_gender
              global temp_password
              global temp_email
              global temp_phone
    
        
              temp_name=StringVar()
              temp_age=StringVar()
              temp_gender=StringVar()
              temp_password=StringVar()
              temp_email=StringVar()
              temp_phone=StringVar()

              e1=ct.CTkEntry(Register_screen,textvariable=temp_name)
              e1.place(x=300,y=100)
        
              e2=ct.CTkEntry(Register_screen,textvariable=temp_age)
              e2.place(x=300,y=150)
        
              e3=ct.CTkEntry(Register_screen,textvariable=temp_gender)
              e3.place(x=300,y=200)
        
              e4=ct.CTkEntry(Register_screen,show='*',textvariable=temp_password)
              e4.place(x=300,y=250)
        
              e5=ct.CTkEntry(Register_screen,textvariable=temp_email)
              e5.place(x=300,y=300)
        
              e6=ct.CTkEntry(Register_screen,textvariable=temp_phone)
              e6.place(x=300,y=350)


              b1=ct.CTkButton(Register_screen,text="Register now",font=('Portico Diagonal',15),command=finish_reg)
              b1.place(x=300,y=400)

       def finish_reg():
              print('done')
              name=temp_name.get()
              age=temp_age.get()
              gender=temp_gender.get()
              password=temp_password.get()
              email=temp_email.get()
              pn=temp_phone.get()

              if name=="" or age=="" or gender=="" or password=="" or email=="" or pn=="":
                     notif1.config(fg="red",text="All fields need to be filled")
              elif (re.fullmatch(regex, email)):
                     pass
              else:
                     notif1.config(fg="red",text="invalid email entered")
              chk=0
              x="use project;"
              cur.execute(x)
              query="select name from details;"
              cur.execute(query)
              data=cur.fetchall()
              print(data)
              for i in data:
                     if name in i:
                            notif1.config(fg="red",text="Account already exists")
                            chk+=1
                     else:
                            notif1.config(fg='green',text='Registration successful',font=('Calibri,36'))
              if chk==0:        
                     x="use project;"
                     cur.execute(x)
                     query3="insert into details (NAME,AGE,Gender,Phone_no,EMAIL,password) values('{}',{},'{}',{},'{}','{}');".format(name,age,gender,pn,email,password)
                     cur.execute(query3)
                     cnx.commit()


# Welcome Page 
       label=ct.CTkLabel(root,text='Welcome to PES International Bank',font=('Arial',22),text_color='White')
       photo1=ct.CTkImage(dark_image=Image.open("C:\\Users\\samya\\Downloads\\Logo3.png"),size=(350,250))
       label.place(x=100,y=250)
       label2=ct.CTkLabel(root,image=photo1,text="")
       label2.place(x=100)
       button1=ct.CTkButton(root,text='Log in')
       button1.place(x=100,y=300)
       button2=ct.CTkButton(root,text='Sign Up',command=registration)
       button2.place(x=310,y=300)

root.mainloop()












    
  
         


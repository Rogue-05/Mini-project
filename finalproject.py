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

cnx=mysql.connect(user='root',password='SQL123',host='localhost')

if cnx.is_connected():
       print('connected')
       cur=cnx.cursor()
       cur.execute('create database if not exists project;')
       cur.execute('use project;')
       q1="create table if not exists new_details(Account_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,NAME varchar(50) NOT NULL,AGE int NOT NULL,Gender varchar(2),Phone_no BIGINT,EMAIL varchar(50),password varchar(10) NOT NULL,BALANCE int Default 10000);"
       cur.execute(q1)
       history1="create table if not exists trans_history(Account_sender int NOT NULL PRIMARY KEY,NAME_rec varchar(50) NOT NULL,Account_rec int NOT NULL,TRANSFERED_AMT int NOT NULL,Balance_before int NOT NULL,BALANCE_after int NOT NULL,TRANS_TYPE varchar(20) Default 'AMOUNT SENT');"
       cur.execute(history1)
       history2="create table if not exists rec_history(acc_of_receiver int NOT NULL PRIMARY KEY,name_of_sender varchar(50) NOT NULL,Account_sender int NOT NULL,TRANSFERED_AMT int NOT NULL,Balance_before int NOT NULL,BALANCE_after int NOT NULL,TRAN_TYPE varchar(20) Default 'AMOUNT RECEIVED');"
       cur.execute(history2)
       

       def login():
              global notif2
              global login_Screen
              global temp_password
              global temp_slno

              login_Screen=Toplevel(root)
              login_Screen.title("login")
              login_Screen.geometry("1000x500")
              login_Screen.configure(background='#252525')

              
              temp_slno = StringVar()
              temp_password = StringVar()
              
              l1=ct.CTkLabel(login_Screen,text=" ** Enter Your details here ** ",font=('Portico Diagonal',26),text_color='white')
              l1.place(x=50)
              l2=ct.CTkLabel(login_Screen,text=" Account Number ",font=('Portico Diagonal',22),text_color='white')
              l2.place(x=50,y=50)
              l3=ct.CTkLabel(login_Screen,text=" password ",font=('Portico Diagonal',22),text_color='white')
              l3.place(x=50,y=100)
              e1=ct.CTkEntry(login_Screen,textvariable=temp_slno)
              e1.place(x=300,y=50)
              e2=ct.CTkEntry(login_Screen,textvariable=temp_password,show='*')
              e2.place(x=300,y=100)
              b1=ct.CTkButton(login_Screen,text="Login",font=('Portico Diagonal',20),command=finish_login)
              b1.place(x=300,y=150)
              b2=ct.CTkButton(login_Screen,text="Forgot password",font=('Portico Diagonal',20),command=forgot_password)
              b2.place(x=50,y=150)
              notif2=ct.CTkLabel(login_Screen,text="",font=('Portico Diagonal',22))
              notif2.place(x=50,y=200)
              

       def finish_login():
            
            global acc_no
            global passwd
            global slno
            global pwd
            global chk
            global name

            name=StringVar()
            slno=int(temp_slno.get())
            pwd=temp_password.get()
            query="select * from new_details;"
            cur.execute(query)
            data=cur.fetchall()
            chk=0

            for i in data:
                acc_no=i[0]
                passwd=i[6]
                name=i[1]

                if acc_no==slno and passwd==pwd:
                    chk+=1
                    break
            if chk==1:
                    global dashboard
                    print("Your account has been found")
                    notif2.configure(fg_color='green',text="Login Successful !")
                    login_Screen.destroy()
                    dashboard=Toplevel(root)
                    dashboard.geometry("1000x1000")
                    dashboard.title("Dashboard")
                    dashboard.configure(background='#252525')

                    photo1=ct.CTkImage(dark_image=Image.open("C:\\Users\\samya\\Downloads\\Logo3.png"),size=(150,100))

                    l2=ct.CTkLabel(dashboard,text='',image=photo1)
                    l2.place(x=75,y=35)
                    l1=ct.CTkLabel(dashboard,text='Welcome to PESIB, '+str(name),font=('Portico Diagonal',30),text_color='white')
                    l1.place(x=25)
                    b1=ct.CTkButton(dashboard,text='Account Details',font=('Portico Diagonal',22),bg_color='#252525',command=acc_details)
                    b1.place(x=25,y=150)
                    b2=ct.CTkButton(dashboard,text='Transaction',font=('Portico Diagonal',22),bg_color='#252525',command=transfer)
                    b2.place(x=25,y=200)
                    b3=ct.CTkButton(dashboard,text='Transfer History',font=('Portico Diagonal',22),bg_color='#252525')
                    b3.place(x=25,y=250)
                    b4=ct.CTkButton(dashboard,text='Cards',font=('Portico Diagonal',22),bg_color='#252525',command=cards)
                    b4.place(x=25,y=300)
                    b5=ct.CTkButton(dashboard,text='Log out',font=('Portico Diagonal',22),bg_color='#252525',command=des)
                    b5.place(x=25,y=350)
              
                    
                    
            else:
                 
                    notif2.configure(fg_color="red",text="Incorrect Details !")
                    return
       def transfer():
                          global to_acc
                          global to_name
                          global passwd
                          global current_balance_sender
                          global curr_bal_rec
                          global trans_amt
                          global updated_bal_sender
                          global updated_bal_rec
                          global transfer_notif
                          global sender_name
                          global transfer_notif1

                          to_acc=StringVar()
                          trans_amt=StringVar()
                          current_balance_sender=IntVar()
                          passwd=StringVar()
                          to_name=StringVar()
                          curr_bal_rec=IntVar()
                          updated_bal_sender=IntVar()
                          updated_bal_rec=IntVar()
                          sender_name=StringVar()

                          transfer_notif=Toplevel(root)
                          transfer_notif.title("Transfer Screen")
                          transfer_notif.geometry("1000x1000")
                          transfer_notif.configure(background='#252525')
                          
                          lab1=ct.CTkLabel(transfer_notif,text="** Transfer Window **",font=('Portico Diagonal',30),text_color='white')
                          lab1.place(x=25,y=0)
                          lab2=ct.CTkLabel(transfer_notif,text='To Name',font=('Portico Diagonal',22),text_color='white')
                          lab2.place(x=0,y=50)
                          lab3=ct.CTkLabel(transfer_notif,text='To Account_ID',font=('Portico Diagonal',22),text_color='white')
                          lab3.place(x=0,y=100)
                          lab4=ct.CTkLabel(transfer_notif,text='Amount',font=('Portico Diagonal',22),text_color='white')
                          lab4.place(x=0,y=150)
                          lab5=ct.CTkLabel(transfer_notif,text='Password',font=('Portico Diagonal',22),text_color='white')
                          lab5.place(x=0,y=200)

                          ent1=ct.CTkEntry(transfer_notif,textvariable=to_name)
                          ent1.place(x=250,y=50)
                          ent1=ct.CTkEntry(transfer_notif,textvariable=to_acc)
                          ent1.place(x=250,y=100)
                          ent1=ct.CTkEntry(transfer_notif,textvariable=trans_amt)
                          ent1.place(x=250,y=150)
                          ent1=ct.CTkEntry(transfer_notif,textvariable=passwd)
                          ent1.place(x=250,y=200)

                          b1=ct.CTkButton(transfer_notif,text='Transfer Now',font=('Portico Diagonal',22),text_color='white',command=finish_transfer)
                          b1.place(x=250,y=300)
                          transfer_notif1=ct.CTkLabel(transfer_notif,text='',text_color='green',font=('Portico Diagonal',30))
                          transfer_notif1.place(x=100,y=350)

       def finish_transfer():
                          trans1="select * from new_details where Account_ID={};".format(int(acc_no))
                          cur.execute(trans1)
                          trans_data=cur.fetchall()
                          for i in trans_data:
                                current_balance_sender=i[7]
                                trans_pwd=i[6]
                                sender_name=i[1]
                          if passwd.get()==trans_pwd:
                                print("valid password")
                                if int(trans_amt.get())>current_balance_sender or int(trans_amt.get())<=0:
                                      transfer_notif1.configure(text="Invalid Amount",text_color='red')
                                else:
                                     updated_bal_sender=current_balance_sender-int(trans_amt.get())
                                     trans2="update new_details set BALANCE='{}' where Account_ID='{}';".format(updated_bal_sender,int(acc_no))
                                     cur.execute(trans2)
                                     cnx.commit()
                                     trans3="select * from new_details where Account_ID={};".format(int(to_acc.get()))
                                     cur.execute(trans3)
                                     tdata=cur.fetchall()
                                     curr_bal_rec=tdata[0][7]
                                     updated_bal_rec=curr_bal_rec+int(trans_amt.get())
                                     trans4="update new_details set BALANCE={} where Account_ID='{}';".format(updated_bal_rec,int(to_acc.get()))
                                     cur.execute(trans4)
                                     cnx.commit()
                                     trans5="update new_details set BALANCE={} where Account_ID={};".format(updated_bal_sender,acc_no)
                                     cur.execute(trans5)
                                     cnx.commit()
                                     history3="insert into trans_history(Account_sender,NAME_rec,Account_rec,TRANSFERED_AMT,Balance_before,BALANCE_after) values({},'{}',{},{},{},{});".format(acc_no,to_name.get(),int(to_acc.get()),int(trans_amt.get()),current_balance_sender,updated_bal_sender)
                                     cur.execute(history3)
                                     cnx.commit()
                                     history4="insert into rec_history(acc_of_receiver,name_of_sender,Account_sender,TRANSFERED_AMT,Balance_before,BALANCE_after) values({},'{}',{},{},{},{});".format(int(to_acc.get()),sender_name,acc_no,int(trans_amt.get()),curr_bal_rec,updated_bal_rec)
                                     cur.execute(history4)
                                     cnx.commit()
                                     transfer_notif1.configure(text='Transferred Successfully',text_color='green')
       def des():
              dashboard.destroy()
              noti=ct.CTkLabel(root,text='LOG OUT SUCCESSFUL!!',font=('Portico Diagonal',30),text_color='green')
              noti.place(x=100,y=400)

       def acc_details():
                          global det_email,det_balance,det_age,det_pn,det_name

                          q5='select * from new_details where Account_ID={}'.format(acc_no)
                          cur.execute(q5)
                          details_data=cur.fetchall()
                          for i in details_data:
                                det_email=i[5]
                                det_balance=i[7]
                                det_age=i[2]
                                det_pn=i[4]
                                det_name=i[1]
                          global acc_detailspage
                          
                          acc_detailspage=Toplevel(root)
                          acc_detailspage.title("ACCOUNT DETAILS")
                          acc_detailspage.geometry("1200x700")
                          acc_detailspage.configure(background='#18140f')

                          l1=ct.CTkLabel(acc_detailspage,text='NAME',font=('Portico Diagonal',22),text_color='white')
                          l1.place(x=10,y=50)
                          l2=ct.CTkLabel(acc_detailspage,text='** Account Details **',font=('Portico Diagonal',22),text_color='white')
                          l2.place(x=50,y=0)
                          l6=ct.CTkLabel(acc_detailspage,text='Phone Number',font=('Portico Diagonal',22),text_color='white')
                          l6.place(x=10,y=150)
                          l3=ct.CTkLabel(acc_detailspage,text='Email-ID',font=('Portico Diagonal',22),text_color='white')
                          l3.place(x=10,y=250)
                          l4=ct.CTkLabel(acc_detailspage,text='Age',font=('Portico Diagonal',22),text_color='white')
                          l4.place(x=10,y=100)
                          l5=ct.CTkLabel(acc_detailspage,text='Balance',font=('Portico Diagonal',22),text_color='white')
                          l5.place(x=10,y=200)
                          l7=ct.CTkLabel(acc_detailspage,text=''+str(det_balance),font=('Portico Diagonal',22),text_color='white')
                          l7.place(x=200,y=200)
                          l8=ct.CTkLabel(acc_detailspage,text=''+str(det_pn),font=('Portico Diagonal',22),text_color='white')
                          l8.place(x=200,y=150)
                          l9=ct.CTkLabel(acc_detailspage,text=''+str(det_email),font=('Portico Diagonal',22),text_color='white')
                          l9.place(x=200,y=250)
                          la=ct.CTkLabel(acc_detailspage,text=''+str(det_name),font=('Portico Diagonal',22),text_color='white')
                          la.place(x=200,y=50)
                          la1=ct.CTkLabel(acc_detailspage,text=''+str(det_age),font=('Portico Diagonal',22),text_color='white')
                          la1.place(x=200,y=100)

                                  
       def forgot_password():
              global for_pass
              global temp_email1
              global temp_phone1
              global notif4
              global temp_slno1

              temp_phone1=StringVar()
              temp_email1=StringVar()
              temp_slno1=StringVar()


              for_pass=Toplevel(root)
              for_pass.geometry("1000x700")
              for_pass.title("Reset Password")
              for_pass.configure(background='#252525')

              notif4=ct.CTkLabel(for_pass,text='',font=('Portico Diagonal',22))
              notif4.place(x=50,y=250)
              l1=ct.CTkLabel(for_pass,text='**Enter your details**',font=('Portico Diagonal',30),)
              l1.place(x=50,y=0)
              l2=ct.CTkLabel(for_pass,text="Account ID -",font=('Portico Diagonal',22))
              l2.place(x=50,y=50)
              l3=ct.CTkLabel(for_pass,text="Email ID -",font=('Portico Diagonal',22))
              l3.place(x=50,y=100)
              l4=ct.CTkLabel(for_pass,text="Phone Number -",font=('Portico Diagonal',22))
              l4.place(x=50,y=150)
              e1=ct.CTkEntry(for_pass,textvariable=temp_slno1)
              e1.place(x=300,y=50)
              e2=ct.CTkEntry(for_pass,textvariable=temp_email1)
              e2.place(x=300,y=100)
              e3=ct.CTkEntry(for_pass,textvariable=temp_phone1)
              e3.place(x=300,y=150)
              b1=ct.CTkButton(for_pass,bg_color='#252525',text='Proceed',command=finish_forgpwd)
              b1.place(x=300,y=200)
              
       def finish_forgpwd():
              global temp_newpwd
              temp_newpwd=StringVar()
              global acc_no1
              acc_no1=int(temp_slno1.get())
              x1="select * from new_details where Account_ID='{}';".format(acc_no1)
              cur.execute(x1)
              data=cur.fetchall()
              if data==[]:
                     notif4.configure(text='Invalid Account number',fg_color='red')
              else:
                     for i in data:
                            if i[4]==int(temp_phone1.get()) and i[5]==str(temp_email1.get()):
                                   notif4.configure(text='Verified!',fg_color='green')

                                   global notif5

                                   final_forgscreen=Toplevel(root)
                                   final_forgscreen.geometry("1000x500")
                                   final_forgscreen.title("Update Password")
                                   final_forgscreen.configure(background='#252525')

                                   l1=ct.CTkLabel(final_forgscreen,text='New password',font=('Portico Diagonal',22),text_color='white')
                                   l1.place(x=25,y=50)
                                   l2=ct.CTkLabel(final_forgscreen,text='*Update password here*',font=('Portico Diagonal',30),text_color='white')
                                   l2.place(x=50)
                                   e1=ct.CTkEntry(final_forgscreen,textvariable=temp_newpwd,show='*')
                                   e1.place(x=325,y=50)
                                   b1=ct.CTkButton(final_forgscreen,bg_color='#252525',text="Confirm",command=update_psswd)
                                   b1.place(x=325,y=100)
                                   notif5=ct.CTkLabel(final_forgscreen,text="",font=('Portico Diagonal',20),fg_color='green')
                                   notif5.place(x=50,y=150)
                            else:
                                   notif4.configure(text='Invalid Details!',fg_color='red')
       def update_psswd():
              if len(temp_newpwd.get())==0:
                     notif5.configure(text='New Password can not be empty',fg_color='red')
              else:
                     newp=temp_newpwd.get()
                     x="update new_details set password='{}' where Account_ID={};".format(newp,acc_no1)
                     cur.execute(x)
                     cnx.commit()
                     notif5.configure(text='Password Successfully changed',fg_color='green')



       def registration():
              Register_screen=Toplevel(root)
              Register_screen.title("Registration")
              Register_screen.geometry("1200x1200")
              Register_screen.configure(background='#252525')
       
        
              global notif1
              global notif3

              notif1=ct.CTkLabel(Register_screen,text="",font=('Portico Diagonal',36),text_color='white')
              notif1.place(x=50,y=450)
              notif3=ct.CTkLabel(Register_screen,text="",font=('Portico Diagonal',26),text_color='white')
              notif3.place(x=50,y=500)
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

       def cards():

              global card_screen
              global photo2

              card_screen=Toplevel(root)
              card_screen.title("Card Details")
              card_screen.geometry("1300x1000")
              card_screen.configure(background='#252525')

              lab1=ct.CTkLabel(card_screen,text='** Your Cards display **',font=('Portico Diagonal',26),text_color='white')
              lab1.place(x=100,y=0)
              b1=ct.CTkButton(card_screen,text='New Card',font=('Portico Diagonal',20),bg_color='#252525',command=new_card)
              b1.place(x=200,y=400)
              if True:
                     photo2=ct.CTkImage(dark_image=Image.open("C:\\Users\\samya\\Downloads\\PngItem_2918764.png"),size=(500,300))
                     lab2=ct.CTkLabel(card_screen,text='',image=photo2)
                     lab2.place(x=50,y=50)

       def new_card():
              card_create=Toplevel(root)
              card_create.title("NEW CARD PAGE")
              card_create.geometry("1300x1000")
              card_create.configure(background='#252525')

              lab1=ct.CTkLabel(card_create,text='** Your new card **',font=('Portico Diagonal',30),text_color='white')
              lab1.place(x=50,y=0)
              lab2=ct.CTkLabel(card_create,text='',image=photo2)
              lab2.place(x=50,y=100)


       def finish_reg():

              global acc_no
              global age1
              global pn1

              acc_no=StringVar()

              print('done')
              name=temp_name.get()
              age=(temp_age.get())
              gender=temp_gender.get()
              password=temp_password.get()
              email=temp_email.get()
              pn=(temp_phone.get())
              
              age1=int(age)
              pn1=int(pn)
              if name=="" or age=="" or gender=="" or password=="" or email=="" or pn=="":
                     notif1.configure(fg_color="red",text="All fields need to be filled",font=('Portico Diagonal',16))
              if bool((re.fullmatch(regex, email)))==True:
                     chk=0
                     x="use project;"
                     cur.execute(x)
                     query="select name from new_details;"
                     cur.execute(query)
                     data=cur.fetchall()
                     print(data)
                     for i in data:
                          if name in i:
                            notif1.configure(fg_color="red",text="Account already exists",font=('Portico Diagonal',16))
                            chk+=1
                          else:
                            notif1.configure(fg_color='green',text='Registration successful',font=('Portico Diagonal',20))
                     if chk==0:        
                          x="use project;"
                          cur.execute(x)
                          query3="insert into new_details (NAME,AGE,Gender,Phone_no,EMAIL,password) values('{}',{},'{}',{},'{}','{}');".format(name,age1,gender,pn1,email,password)
                          cur.execute(query3)
                          cnx.commit()
                          y="select Account_ID from new_details where password='{}' and EMAIL='{}';".format(password,email)
                          cur.execute(y)
                          data=cur.fetchone()
                          acc_no=str(data[0])
                          notif3.configure(text="Account number generated : "+acc_no,fg_color='green')

              else:
                     notif1.configure(fg_color="red",text="invalid email entered",font=('Portico Diagonal',22))
              



# Welcome Page 

       label=ct.CTkLabel(root,text='Welcome to PES International Bank',font=('Arial',22),text_color='White')
       photo1=ct.CTkImage(dark_image=Image.open("C:\\Users\\samya\\Downloads\\Logo3.png"),size=(350,250))
       label.place(x=100,y=250)
       label2=ct.CTkLabel(root,image=photo1,text="")
       label2.place(x=100)
       button1=ct.CTkButton(root,text='Log in',command=login)
       button1.place(x=100,y=300)
       button2=ct.CTkButton(root,text='Sign Up',command=registration)
       button2.place(x=310,y=300)
       
       

root.mainloop()













    
  
         














    
  
         

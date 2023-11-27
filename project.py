from tkinter import *
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 

   
root = Tk() 
root.title('PES INTERNATIONAL BANK')
root.geometry('1000x1000')
cnx=mysql.connect(user='root',password='Rogue@05',host='localhost')


if cnx.is_connected():
  print('connected')
  cur=cnx.cursor()
  cur.execute('create database if not exists project;')
  cur.execute('use project;')
  q1=''' create table if not exists details(
         slno int NOT NULL AUTO_INCREMENT PRIMARY KEY,
         NAME varchar(50) NOT NULL,
         AGE int NOT NULL,
         Gender varchar(2),
         Phone_no int(10),
         EMAIL varchar(50),
         password varchar(10) NOT NULL,
         BALANCE int Default 1000)'''
  cur.execute(q1)
  def registration():
        Register_screen=Toplevel(root)
        Register_screen.title("Registration")
        global notif1
        notif1=Label(Register_screen,font=('Calibri',36))
        notif1.grid(row=9,sticky=N)
        l1=Label(Register_screen,text="ENTER YOUR DETAILS PLEASE",font=('Çalibri',36))
        l1.grid(row=0,sticky=N)
        l2=Label(Register_screen,text="Name",font=('Calibri',24))
        l2.grid(row=1,sticky=W)
        l3=Label(Register_screen,text="Age",font=('Calibri',24))
        l3.grid(row=2,sticky=W)
        l4=Label(Register_screen,text="Gender(M/F)",font=('Calibri',24))
        l4.grid(row=3,sticky=W)
        l5=Label(Register_screen,text="Password",font=('Calibri',24))
        l5.grid(row=6,sticky=W)
        l6=Label(Register_screen,text="Email",font=('calibri',24))
        l6.grid(row=5,sticky=W)
        l7=Label(Register_screen,text='Phone Number',font=('calibri',24))
        l7.grid(row=4,sticky=W)
        global temp_name
        global temp_age
        global temp_gender
        global temp_password
        global temp_email
        global temp_phone
    
        
        temp_name=StringVar()
        temp_age=IntVar()
        temp_gender=StringVar()
        temp_password=StringVar()
        temp_email=StringVar()
        temp_phone=IntVar()

        e1=Entry(Register_screen,text=temp_name,width=20)
        e1.grid(row=1)
        
        e2=Entry(Register_screen,text=temp_age,width=20)
        e2.grid(row=2)
        
        e3=Entry(Register_screen,text=temp_gender,width=20)
        e3.grid(row=3)
        
        e4=Entry(Register_screen,text=temp_password,width=20)
        e4.grid(row=6)
        
        e5=Entry(Register_screen,text=temp_email,width=20)
        e5.grid(row=5)
        
        e6=Entry(Register_screen,text=temp_phone,width=20)
        e6.grid(row=4)
        

        b1=Button(Register_screen,text="Register now",command=finish_reg,padx=100)
        b1.grid(row=8)

def finish_reg():
  print('done')
  nam=temp_name.get()
  age=temp_age.get()
  gender=temp_gender.get()
  password=temp_password.get()
  email=temp_email.get()
  pn=temp_phone.get()

  if nam=="" or age=="" or gender=="" or password=="" or email=="" or pn=="":
            notif1.config(fg="red",text="All fields need to be filled")
  elif(re.fullmatch(regex, email)):
            notif1.config(fg="green",text="registeration success")
  else:
            notif1.config(fg="red",text="invalid email entered")
  chk=0
  x="use project;"
  cur.execute(x)
  query="select name from bank"
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
            query3="insert into bank values(Default,'{}',{},'{}',{},'{}','{}',Default);".format(name,age,gender,phone,email,password)
            cur.execute(query3)
            cnx.commit()











Button(root,text='register',command=registration).pack()

    
  
         


    
  
         


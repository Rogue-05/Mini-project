from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox 
import customtkinter as ctk

root = Tk() 
root.title('PES INTERNATIONAL BANK')
root.geometry('1000x1000')
cxn=mysql.connect(user='root',password='Rogue@05',host='localhost')

if cnx.isconnected():
  print('connected')
  cur=cnx.cursor()
  cur.execute('create database if not exists')


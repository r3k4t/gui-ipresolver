import socket
from tkinter import *
def rkt_Speed_test(): 
	r = socket.gethostbyname(t.get()) 
	k.set(r)  
rkt = Tk() 
rkt.title("GUI IP RESOLVER (RKT)")
rkt.config(bg='dark cyan')
k = StringVar() 
Label(rkt,text='Enter a URL :',bg='dark cyan').grid(row=0, sticky=W) 
Label(rkt,text='IP  Address :',bg='dark cyan').grid(row=2, sticky=W) 
result = Label(rkt,text="", textvariable=k,bg='dark cyan').grid(row=2, column=1, sticky=W) 
t = Entry(rkt) 
t.grid(row=0, column=1) 
b = Button(rkt,text='Check',bg='dark cyan',command=rkt_Speed_test) 
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=3, pady=3) 
rkt.mainloop() 

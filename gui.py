import tkinter
import os

lk=tkinter.Tk()
lk.title("grid demo")
lk.geometry('640x480-8-200')
lk['padx']=8
label=tkinter.Label(lk,text="Grid Demo")
label.grid(row=0,column=0,columnspan=3)
lk.columnconfigure(0,weight=1)
lk.columnconfigure(1,weight=1)
lk.columnconfigure(2,weight=3)
lk.columnconfigure(3,weight=3)
lk.columnconfigure(4,weight=3)
lk.rowconfigure(0,weight=1)
lk.rowconfigure(1,weight=10)
lk.rowconfigure(2,weight=1)
lk.rowconfigure(3,weight=3)
lk.rowconfigure(4,weight=3)
fl=tkinter.Listbox(lk)
fl.grid(row=1,column=0,sticky='nesw',rowspan=2)
fl.config(border=2,relief="sunken")
for zone in os.listdir('/Windows/System32'):
    fl.insert(tkinter.END,zone)
ls=tkinter.Scrollbar(lk,orient=tkinter.VERTICAL,command=fl.yview)
ls.grid(sticky='nsw',rowspan=2,row=1,column=1)
fl['yscrollcommand']=ls.set

oframe=tkinter.LabelFrame(lk,text="file deatils")
oframe.grid(row=1,column=2,sticky='ne')
rbvalue=tkinter.IntVar()
rbvalue.set(3)
radio1=tkinter.Radiobutton(oframe,text="filename",value=1,variable=rbvalue)
radio2=tkinter.Radiobutton(oframe,text="path",value=2,variable=rbvalue)
radio3=tkinter.Radiobutton(oframe,text="timestamp",value=3,variable=rbvalue)
radio1.grid(row=1,column=0,sticky='w')
radio2.grid(row=2,column=0,sticky='w')
radio3.grid(row=3,column=0,sticky='w')
rlabel=tkinter.Label(lk,text="result")
rlabel.grid(row=2,column=2,sticky='nw')
result=tkinter.Entry(lk)
result.grid(row=2,column=2,sticky='sw')
tframe=tkinter.LabelFrame(lk,text="timeframe")
tframe.grid(row=3,column=0,sticky='new')

hourspinner=tkinter.Spinbox(tframe,width=2,value=tuple(range(0,24)))
minutespinner=tkinter.Spinbox(tframe,width=2,from_=0,to=59)
secondspinner=tkinter.Spinbox(tframe,width=2,from_=0,to=59)

hourspinner.grid(row=0,column=0)
tkinter.Label(tframe,text=":").grid(row=0,column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(tframe,text=":").grid(row=0,column=3)
secondspinner.grid(row=0,column=4)
tframe['padx']=36

dateframe=tkinter.Frame(lk)
dateframe.grid(row=4,column=0,sticky='new')
daylabel=tkinter.Label(dateframe,text="day")
monthlabel=tkinter.Label(dateframe,text="month")
yearlabel=tkinter.Label(dateframe,text="year")
daylabel.grid(row=0,column=0,sticky='w')
monthlabel.grid(row=0 ,column=1,sticky='w')
yearlabel.grid(row=0,column=2,sticky='w')

dayspin=tkinter.Spinbox(dateframe,width=5,from_=1,to=31)
monnthspin=tkinter.Spinbox(dateframe,width=5,values=("jan","feb","mar","april","may","Jun","jul","aug","sept","oct","nov","Dec"))
yearspin=tkinter.Spinbox(dateframe,width=5,from_=1990,to=2090)
dayspin.grid(row=1,column=0)
monnthspin.grid(row=1,column=1)
yearspin.grid(row=1,column=2)

okbutteon=tkinter.Button(lk,text="OK")
okbutteon.grid(row=3,column=3,sticky='e')
cancelbutteon=tkinter.Button(lk,text="Cancel",command=lk.quit)
cancelbutteon.grid(row=3,column=4,sticky='w')
lk.mainloop()
print(rbvalue.get())
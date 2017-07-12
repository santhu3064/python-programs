import tkinter

try:
	import _tkinter
except ImportError:
	import Tkinter as tkinter
#print(tkinter.TkVersion)
#print(tkinter.TclVersion)
#tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("New blog")
mainWindow.geometry('640x480')
lable=tkinter.Label(mainWindow,text="Hello world")
lable.pack(side='top')
leftFrame=tkinter.Frame(mainWindow)
leftFrame.pack(sid='left',anchor='n',fill=tkinter.Y,expand=False)
canvas=tkinter.Canvas(mainWindow,relief='raised', borderwidth=1)
canvas.pack(side='left',anchor='n')
rightFrame=tkinter.Frame(mainWindow)
rightFrame.pack(sid='right',anchor='n',expand=True)
button1=tkinter.Button(rightFrame,text='Button1')
button2=tkinter.Button(rightFrame,text='Button2')
button3=tkinter.Button(rightFrame,text='Button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()
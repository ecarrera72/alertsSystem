from tkinter import *
from time import *
import threading
import os

class alertsInterface(object):
    
    def __init__(self):
        root = Tk()
        #root.geometry('1365x800')
        root.geometry('1365x650')
        root.resizable(width=False, height=False)
        self.dateTime = StringVar()
        path, _ = os.path.split(os.path.realpath(__file__))
        back = PhotoImage(file = path + "/images/background.png")

        Label(root, image = back, bd = 0, bg = 'black').place(x = 0, y = 0)
        Label(root, textvariable = self.dateTime, bg = 'black', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 60, y = 60)
        Label(root, text = 'SISTEMA DE ALERTAS', bg = 'black', fg = 'yellow', font= ('verdana', 30, 'bold')).place(x = 435, y = 180)
        Label(root, text = 'FECHA', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold')).place(x = 50, y = 230)
        Label(root, text = 'HORA', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold')).place(x = 230, y = 230)
        Label(root, text = 'EQUIPO', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold')).place(x = 380, y = 230)
        Label(root, text = 'MENSAJE', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold')).place(x = 650, y = 230)

        Label(root, text = strftime("%d-%m-%Y"), bg = 'black', fg = 'orange', font= ('verdana', 18, 'bold')).place(x = 50, y = 280)
        Label(root, text = strftime("%H:%M:%S"), bg = 'black', fg = 'orange', font= ('verdana', 18, 'bold')).place(x = 230, y = 280)
        Label(root, text = 'VALIDADORA', bg = 'black', fg = 'orange', font= ('verdana', 18, 'bold')).place(x = 380, y = 280)
        Label(root, text = 'PAPEL CERCA DE TERMINARSE', bg = 'black', fg = 'orange', font= ('verdana', 18, 'bold')).place(x = 650, y = 280)
        #equipo = Label(root, text = 'EQUIPO:', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold'))
        #equipo.place(x = 470, y = 250)
        #equipoText = Label(root, text = 'EXPEDIDORA', bg = 'black', fg = 'orange', font= ('verdana', 25, 'bold'))
        #equipoText.place(x = 650, y = 250)

        #equipo = Label(root, text = 'MENSAJE:', bg = 'black', fg = 'green', font= ('verdana', 25, 'bold'))
        #equipo.place(x = 443, y = 300)
        #equipoText = Label(root, text = 'PAPEL CERCA DE TERMINARSE', bg = 'black', fg = 'orange', font= ('verdana', 25, 'bold'))
        #equipoText.place(x = 650, y = 300)

        threading.Thread(target=self.dateTimeAct).start()

        

        root.mainloop()
    
    def dateTimeAct(self):
        while True:
            self.dateTime.set(strftime("%d-%m-%Y %H:%M:%S"))
            sleep(1)



alertsInterface()
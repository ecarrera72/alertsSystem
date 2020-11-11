from tkinter import *
from time import *
import threading
import os

class alertsInterface(object):
    
    def __init__(self):
        root = Tk()
        #root.geometry('1365x800')
        root.geometry('1280x700')
        root.resizable(width=False, height=False)
        #root.overrideredirect(True)
        
        #scroll = Scrollbar(root)
        #scroll.place(x = 660, y = 170)

        self.dateTime = StringVar()
        path, _ = os.path.split(os.path.realpath(__file__))
        back = PhotoImage(file = path + "/images/svrMonitoreo.png")
        Label(root, image = back, bd = 0, bg = 'black').place(x = 0, y = 0)
        
        Label(root, textvariable = self.dateTime, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 1075, y = 25)

        svrGreen = PhotoImage(file = path + "/images/equipo/server_green.png").subsample(3)
        Label(root, image = svrGreen, bd = 0, bg = '#303030').place(x = 80, y = 575)

        tpvGren = PhotoImage(file = path + "/images/equipo/estacion_green.png").subsample(3)
        Label(root, image = tpvGren, bd = 0, bg = '#303030').place(x = 190, y = 575)

        expGreen = PhotoImage(file = path + "/images/equipo/expedidora_green.png").subsample(3)
        Label(root, image = expGreen, bd = 0, bg = '#303030').place(x = 300, y = 575)

        Label(root, image = expGreen, bd = 0, bg = '#303030').place(x = 410, y = 575)

        payGreen = PhotoImage(file = path + "/images/equipo/Paystation_Verde.png").subsample(31)
        Label(root, image = payGreen, bd = 0, bg = '#303030').place(x = 520, y = 575)

        svrGreenAct = PhotoImage(file = path + "/images/equipo/server_green.png")
        Label(root, image = svrGreenAct, bd = 0, bg = '#303030').place(x = 40, y = 170)

        #scroll = Scrollbar(root, )
        listbox = Listbox(root, activestyle = NONE, border=0, bg = '#303030', highlightthickness = 0, 
                            fg = 'white', width = 71, height = 19)
        listbox.place(x = 660, y = 165)

        #listbox.insert(0, svrGreenAct)
        #listbox.insert(0, path + "/images/equipo/server_green.png")

        
        #listbox.pack()

        #svrGreenEve = PhotoImage(file = path + "/images/equipo/server_green.png")
        #Label(root, image = svrGreen, bd = 0, bg = '#303030')#.place(x = 660, y = 170)
        #Label(root, text = 'info del evento', bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 760, y = 190)
        listbox.insert(0, svrGreen)
        #Label(root, image = tpvGren, bd = 0, bg = '#303030').place(x = 660, y = 280)
        #Label(root, text = 'info del evento', bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 760, y = 300)

        #Label(root, image = expGreen, bd = 0, bg = '#303030').place(x = 660, y = 390)
        #Label(root, text = 'info del evento', bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 760, y = 410)
        
        #Label(root, image = payGreen, bd = 0, bg = '#303030').place(x = 660, y = 460)
        #Label(root, text = 'info del evento', bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 760, y = 460)

        threading.Thread(target=self.dateTimeAct).start()        

        root.mainloop()
    
    def dateTimeAct(self):
        while True:
            self.dateTime.set(strftime("%d-%m-%Y\n%H:%M:%S"))
            sleep(1)



alertsInterface()
from queries.queriesMysql import queriesMysql
from controller import controller
from style.style import style
from time import sleep, strftime
import threading, os, sys, logging
from tkinter import Tk, PhotoImage, StringVar, Label, Frame, Canvas, Scrollbar

class alertsInterface(style, controller):
    
    def __init__(self):
        super().__init__()
        print(self.green(strftime("%d-%m-%Y %X") + " Inicia sistema de alertas"))
        var = self.sqliteDataBase()
        dbParking = self.parking(var[0])
        instanceQueries = queriesMysql()
        getEquipos = instanceQueries.

        root = Tk()
        root.geometry('1280x700')
        root.resizable(width=False, height=False)
        #root.overrideredirect(True)
        self.dateTime = StringVar()
        path, _ = os.path.split(os.path.realpath(__file__))
        back = PhotoImage(file = path + "/images/svrMonitoreo.png")
        Label(root, image = back, bd = 0, bg = 'black').place(x = 0, y = 0)
        Label(root, textvariable = self.dateTime, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 1075, y = 25)

        svrGreenAct = PhotoImage(file = path + "/images/equipo/server_green.png")
        Label(root, image = svrGreenAct, bd = 0, bg = '#303030').place(x = 40, y = 170)

        Label(root, text = 'Servidor Liverpool', bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 350, y = 170)

        Label(root, text = 'Boleto Cobrado:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 200)
        Label(root, text = 'Folio: 12345678912\nFecha: 21-12-2020 11:50:35', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 225)
        Label(root, text = 'Boleto Expedido:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 270)
        Label(root, text = 'Folio: 12345678912\nFecha: 21-12-2020 10:58:24', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 295)
        Label(root, text = 'Pensionado Entrada:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 340)
        Label(root, text = 'Tarjeta: 520\nFecha: 21-12-2020 10:58:24', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 365)
        Label(root, text = 'Pensionado Salida:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 410)
        Label(root, text = 'Tarjeta: 520\nFecha: 21-12-2020 10:58:24', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 435)

        Label(root, text = 'Ubicacion: ', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 15, 'bold')).place(x = 80, y = 480)
        Label(root, text = 'Oficina', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 15, 'bold')).place(x = 210, y = 480)

        svrGreen = PhotoImage(file = path + "/images/equipo/server_green.png").subsample(3)
        Label(root, image = svrGreen, bd = 0, bg = '#303030').place(x = 390, y = 540)
        Label(root, text = 'Servidor', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = 390, y = 640)

        tpvGren = PhotoImage(file = path + "/images/equipo/estacion_green.png").subsample(3)
        Label(root, image = tpvGren, bd = 0, bg = '#303030').place(x = 490, y = 540)
        Label(root, text = 'Tpv', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = 490, y = 640)

        expGreen = PhotoImage(file = path + "/images/equipo/expedidora_green.png").subsample(3)
        Label(root, image = expGreen, bd = 0, bg = '#303030').place(x = 590, y = 540)
        Label(root, text = 'Expedidora', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = 590, y = 640)

        Label(root, image = expGreen, bd = 0, bg = '#303030').place(x = 690, y = 540)
        Label(root, text = 'Validadora', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = 690, y = 640)

        payGreen = PhotoImage(file = path + "/images/equipo/Paystation_Verde.png").subsample(31)
        Label(root, image = payGreen, bd = 0, bg = '#303030').place(x = 790, y = 540)
        Label(root, text = 'Paystation', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = 790, y = 640)

        container = Frame(root)
        canvas = Canvas(container, width=550, height=340, bg = '#303030', highlightthickness = 0)
        scrollbar = Scrollbar(container, orient = 'vertical', command = canvas.yview)
        scrollable_frame = Frame(canvas, bg = '#303030')

        scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        canvas.create_window((0,0), window = scrollable_frame, anchor = 'nw')

        canvas.configure(yscrollcommand = scrollbar.set)
        
        Label(scrollable_frame, image = svrGreen, bd = 0, bg = '#303030').grid(row = 0, column = 0)
        Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 0, column = 1)

        Label(scrollable_frame, image = tpvGren, bd = 0, bg = '#303030').grid(row = 1, column = 0)
        Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 1, column = 1)

        Label(scrollable_frame, image = expGreen, bd = 0, bg = '#303030').grid(row = 2, column = 0)
        Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 2, column = 1)

        Label(scrollable_frame, image = payGreen, bd = 0, bg = '#303030').grid(row = 3, column = 0)
        Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 3, column = 1)

        Label(scrollable_frame, image = expGreen, bd = 0, bg = '#303030').grid(row = 4, column = 0)
        Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 4, column = 1)

        container.place(x = 660, y = 165)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        threading.Thread(target=self.dateTimeAct).start()

        root.mainloop()
    
    def dateTimeAct(self):
        try:
            while True:
                self.dateTime.set(strftime("%d-%m-%Y\n%X"))
                sleep(1)
        except Exception as e:
            print(self.red(e))

alertsInterface()
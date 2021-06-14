from queries.queriesMysql import queriesMysql
from controller import controller
from style.style import style
from time import sleep, strftime
import threading, os, sys, logging
from tkinter import Button, Tk, PhotoImage, StringVar, Label, Frame, Canvas, Scrollbar

class alertsInterface(style, controller):
    
    def __init__(self):
        super().__init__()
        print(self.green(strftime("%d-%m-%Y %X") + " Inicia sistema de alertas"))
        var = self.sqliteDataBase()
        dbParking = self.parking(var[0])
        instanceQueries = queriesMysql()
        getTipoEquipo = instanceQueries.getTipoEquipo(dbParking)
        getEquipos = instanceQueries.getEquipo(dbParking)

        root = Tk()
        root.geometry('1280x700')
        root.resizable(width=False, height=False)
        #root.overrideredirect(True)
        self.dateTime = StringVar()
        self.nameEquipo = StringVar() # SERVIDOR
        self.infoBolCobrado = StringVar() # Folio: 12345678912\nFecha: 21-12-2020 11:50:35
        self.infoBolExpedido = StringVar() # Folio: 12345678912\nFecha: 21-12-2020 11:50:35
        self.infoTarjEntrada = StringVar() # Tarjeta: 520\nFecha: 21-12-2020 10:58:24
        self.infoTarjSalida = StringVar() # Tarjeta: 520\nFecha: 21-12-2020 10:58:24
        self.ubicacion = StringVar() # Oficina
        path, _ = os.path.split(os.path.realpath(__file__))
        back = PhotoImage(file = path + "/images/svrMonitoreo.png")
        Label(root, image = back, bd = 0, bg = 'black').place(x = 0, y = 0)
        Label(root, textvariable = self.dateTime, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 1075, y = 25)

        equipos = self.arrayEquipos(getTipoEquipo, path, 4)
        equipoAct = self.arrayEquipos(getTipoEquipo, path, 1)

        #------------------------------- Alerta Actual ----------------------------------------------------
        self.infoEquipo(root, equipoAct, 2, 'SERVIDOR', 'SERVER', instanceQueries, dbParking)

        #------------------------------ Inventario Equipo -------------------------------------------------
        ejeX, ejeY, avanzaEjeX, textEjeY= 80, 578, 90, 660
        data = []

        for equipo in getEquipos:
            boton = Button(root, image = equipos[equipo['t_equipo_descripcion']], bg = '#303030', bd = 0, 
                    command = lambda: self.infoEquipo(root, equipoAct, equipo['inv_eq_neg_Id_Usuarios'] , 
                    equipo['t_equipo_descripcion'], equipo['Usuario'], instanceQueries, dbParking)).place(x = ejeX, y = ejeY)
            Label(root, text = equipo['Usuario'], bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 9, 'bold')).place(x = ejeX, y = textEjeY)

            data.append(boton)

            ejeX += avanzaEjeX
        #----------------------------- Eventos del Dia ----------------------------------------------------
        # container = Frame(root)
        # canvas = Canvas(container, width=550, height=340, bg = '#303030', highlightthickness = 0)
        # scrollbar = Scrollbar(container, orient = 'vertical', command = canvas.yview)
        # scrollable_frame = Frame(canvas, bg = '#303030')

        # scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # canvas.create_window((0,0), window = scrollable_frame, anchor = 'nw')

        # canvas.configure(yscrollcommand = scrollbar.set)
        
        # Label(scrollable_frame, image = svrGreen, bd = 0, bg = '#303030').grid(row = 0, column = 0)
        # Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 0, column = 1)

        # Label(scrollable_frame, image = tpvGren, bd = 0, bg = '#303030').grid(row = 1, column = 0)
        # Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 1, column = 1)

        # Label(scrollable_frame, image = expGreen, bd = 0, bg = '#303030').grid(row = 2, column = 0)
        # Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 2, column = 1)

        # Label(scrollable_frame, image = payGreen, bd = 0, bg = '#303030').grid(row = 3, column = 0)
        # Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 3, column = 1)

        # Label(scrollable_frame, image = expGreen, bd = 0, bg = '#303030').grid(row = 4, column = 0)
        # Label(scrollable_frame, text = 'info del evento', bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 13, 'bold')).grid(row = 4, column = 1)

        # container.place(x = 660, y = 165)
        # canvas.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")

        threading.Thread(target=self.dateTimeAct).start()

        root.mainloop()
    
    def dateTimeAct(self):
        try:
            while True:
                self.dateTime.set(strftime("%d-%m-%Y\n%X"))
                sleep(1)
        except Exception as e:
            print(self.red(e))
    
    def arrayEquipos(self, tipoEquipos, path, minimizar):
        array = {}
        for x in tipoEquipos:
            imgMinimiza = minimizar
            if x['t_equipo_id'] == 5: imgMinimiza = minimizar * 10

            ruta = "{}/images/equipo/{}.png".format(path, x['t_equipo_descripcion'])
            array[x['t_equipo_descripcion']] = PhotoImage(file = ruta).subsample(imgMinimiza)

        return array
    
    def infoEquipo(self, root, equipoAct, idEquipo, tEquipo, nameEquipo, instanceQueries, dbParking):
        print(tEquipo)
        print(nameEquipo)
        info = instanceQueries.getInfoEquipo(dbParking)

        bolE = 'Folio: {}\nFecha: {} {}'.format(info['bolE']['Id_Movimientos'], info['bolE']['Fecha_Entrada'], info['bolE']['Hora_Entrada'])
        
        bolC = 'Folio: {}\nFecha: {} {}'.format(info['bolS']['Id_Movimientos'], info['bolS']['Fecha_Salida'], info['bolS']['Hora_Salida'])

        tarjE = 'Tarjeta: {}\nFecha: {} {}'.format(info['tarjE']['mope_tarj_id'], info['tarjE']['mope_fecha'], info['tarjE']['mope_hora'])                                        

        tarjS = 'Tarjeta: {}\nFecha: {} {}'.format(info['tarjS']['mope_tarj_id'], info['tarjS']['mope_fecha'], info['tarjS']['mope_hora'])

        Label(root, image = equipoAct[tEquipo], bd = 0, bg = '#303030').place(x = 40, y = 170)
        Label(root, text = nameEquipo, bd = 0, bg = '#303030', fg = 'white', font= ('verdana', 15, 'bold')).place(x = 350, y = 170)
        Label(root, text = 'Boleto Cobrado:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 200)
        Label(root, text = bolC, bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 225)
        Label(root, text = 'Boleto Expedido:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 270)
        Label(root, text = bolE, bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 295)
        Label(root, text = 'Pensionado Entrada:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 340)
        Label(root, text = tarjE, bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 365)
        Label(root, text = 'Pensionado Salida:', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 13, 'bold')).place(x = 350, y = 410)
        Label(root, text = tarjS, bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 10, 'bold')).place(x = 390, y = 435)
        Label(root, text = 'Ubicacion: ', bd = 0, bg = '#303030', fg = '#338aff', font= ('verdana', 15, 'bold')).place(x = 80, y = 480)
        Label(root, text = self.ubicacion, bd = 0, bg = '#303030', fg = '#a9cce3', font= ('verdana', 15, 'bold')).place(x = 210, y = 480)


alertsInterface()
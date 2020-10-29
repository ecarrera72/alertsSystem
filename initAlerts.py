from style.style import style
from time import *

class initAlerts(style):
    
    def __init__(self):
        print(self.green("Inicia alertas de sistema " + strftime("%d-%m-%Y %H:%M:%S")))

initAlerts()
from style.style import style
from models import models
from time import *

class initAlerts(style, models):
    
    def __init__(self):
        super().__init__()
        print(self.green("Inicia alertas de sistema " + strftime("%d-%m-%Y %H:%M:%S")))
        

initAlerts()
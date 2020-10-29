from style.style import style
from time import *
import os

class config(style):
    _coding = None
    _dataDBP = None
    _dataDBT = None

    def __init__(self, varDB, coding):
        if self._coding is None: self._coding = coding
        self.checkMac(varDB)
    
    def telemetria(self, connectType, varDB):
        self._dataDBT = self.configData(connectType, varDB)
        if self._dataDBT is not None: self._dataDBT['database'] = varDB['TELEMETRIADB']
        return self._dataDBT
    
    def parking(self, connectType, varDB):
        self._dataDBP = self.configData(connectType, varDB)
        if self._dataDBP is not None: self._dataDBP['database'] = varDB['PARKINGDB']
        return self._dataDBP
    
    def configData(self, connectType, varDB):
        if connectType == "local":
            data = {
                'user' : str(self._coding.decode(varDB['LOCAL_USERDB'][1:], varDB['LOCAL_USERDBF'])),
                'password' : str(self._coding.decode(varDB['LOCAL_PASSWDDB'][1:], varDB['LOCAL_PASSWDDBF'])),
                'host' : str(varDB['LOCAL_HOSTDB']),
                'port' : int(varDB['LOCAL_PORTDB'])
            }

        elif connectType == "remote":
            data = {
                'user' : str(self._coding.decode(varDB['REMOTE_USERDB'][1:], varDB['REMOTE_USERDBF'])),
                'passwd' : str(self._coding.decode(varDB['REMOTE_PASSWDDB'][1:], varDB['REMOTE_PASSWDDBF'])),
                'host' : str(varDB['REMOTE_HOSTDB']),
                'port' : int(varDB['REMOTE_PORTDB'])
            }
        
        return data
        
    def checkMac(self, varDB):
        m = self._coding.decode(varDB['MAC_ADDRESS'][1:], varDB['MAC_ADDRESSF'])
        macs = os.popen("cat /sys/class/net/*/address").read()
        for mac in macs.split():
            if m == mac: return True
        
        print(self.red("Error en la mac address"))
        sleep(3)
        os._exit(1)
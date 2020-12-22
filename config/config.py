class config():
    
    def configDataBase(self, varDB):
        data = {
            'user' : str(varDB[1]),
            'password' : str(varDB[2]),
            'host' : str(varDB[3]),
            'database' : str(varDB[4]),
            'port' : int(varDB[5])
        }
        
        return data
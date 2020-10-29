from datetime import datetime

class style:

	def black(self, msj):
		msj = chr(27) + "[1;30m" + str(msj) + chr(27) + "[0m" # texto en negritas de color negro
		return msj.center(90, " ")

	def blackL(self, msj):
		msj = chr(27) + "[1;30m" + str(msj) + chr(27) + "[0m" # texto en negritas de color negro
		return msj

	def red(self, msj):
		msj = chr(27) + "[1;31m" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + chr(32) + str(msj) + chr(27) + "[0m" # texto en negritas de color rojo
		return msj.center(90, " ")

	def green(self, msj):
		msj = chr(27) + "[1;32m" + str(msj) + chr(27) + "[0m" # texto en negritas de color verde
		return msj.center(90, " ")

	def greenS(self, msj):
		msj = chr(27) + "[2;32m" + str(msj) + chr(27) + "[0m" # texto en negritas de color verde
		return msj.center(90, " ")

	def yellow(self, msj):
		msj = chr(27) + "[1;33m" + str(msj) + chr(27) + "[0m" # texto en negritas de color amarillo
		return msj.center(90, " ")

	def blue(self, msj):
		msj = chr(27) + "[1;34m" + str(msj) + chr(27) + "[0m" # texto en negritas de color azul
		return msj.center(90, " ")

	def purple(self, msj):
		msj = chr(27) + "[1;35m" + str(msj) + chr(27) + "[0m" # texto en negritas de color morado
		return msj.center(90, " ")

	def cyan(self, msj):
		msj = chr(27) + "[1;36m" + str(msj) + chr(27) + "[0m" # texto en negritas de color cyan
		return msj.center(90, " ")

	def cyanS(self, msj):
		msj = chr(27) + "[2;36m" + str(msj) + chr(27) + "[0m" # texto debil de color cyan
		return msj.center(90, " ")

	def cyanSL(self, msj):
		msj = chr(27) + "[2;36m" + str(msj) + chr(27) + "[0m" # texto debil de color cyan
		return msj

	def center(self, msj):
		return msj.center(90, " ")
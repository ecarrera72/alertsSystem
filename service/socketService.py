from style.style import style
from time import sleep
import socket, os, logging

class socketService():

	def socketEnvio(self, tipo, command, var):
		if tipo == 'RFID':
			host = str(var['CTE_RFID_HOST_SERSOCKET'])
			port = int(var['CTE_RFID_PORT_SERSOCKET'])

		comand = str(command)

		try:
			serverSocket = socket.socket()
			serverSocket.connect((host, port))
			serverSocket.send(comand.encode())
			serverSocket.close()
			return True
		except Exception as e:
			print("socket envio")
			print(style().red(e))
			logging.error(e)
			return False

	def socketEscucha(self, host, port):
		try:
			serverSocket = socket.socket()
			serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			serverSocket.bind((host, port))
			serverSocket.listen(5)
		except Exception as e:
			print("socket escucha")
			print(style().red(e))
			logging.error(e)
			if os.popen("echo '" + str(e) + "' | grep '[Errno 98]'").read() != "":
				pid = os.popen("sudo lsof -i:" + str(port) + " | awk '{printf $2}'").read().split('PID')[1]
				os.popen("sudo kill -9 " + pid).read()

			print(style().red("Error en socket"))

		return serverSocket
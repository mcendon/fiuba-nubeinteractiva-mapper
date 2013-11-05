import signal, sys, random
import threading
import time
from serial import Serial
#Controlador
class Controlador(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

		self._idle = True
		try:
			self.serial = Serial('/dev/rfcomm0', 19200, timeout = 0.1)
		except Exception as e:
			raise Exception("Error al inicializar puerto: " + str(e))

		self.serial.flushInput() # Para limpiar el buffer de entrada de la compu.
		self.start()

	def isIdle(self):
		return self._idle

	def run(self):
		while True:
			if self.serial.inWaiting() > 0 and self.serial.read().encode('hex') == "55":
				self._idle = True

			time.sleep(0.2)
	
	def hacerEfecto(self,idEfecto):
		if idEfecto != None:
			self._idle = False
			self.serial.write(chr(idEfecto))
			print "[Mensaje del Controlador]: Despache el efecto Id ",idEfecto," a la nube" 
		else:
			print "No hay definido un mapeo para el evento solicitado"
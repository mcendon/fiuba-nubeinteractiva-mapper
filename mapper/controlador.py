import signal, sys, random
#Controlador
class Controlador():
	def isIdle(self):
		return bool(random.randint(0,1))
	
	def hacerEfecto(self,idEfecto):
		if idEfecto != None:
			print "[Mensaje del Controlador]: Despache el efecto Id ",idEfecto," a la nube" 
		else:
			print "No hay definido un mapeo para el evento solicitado"
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import threading, time, signal, sys, random

#Controlador
#Controlador del arduino
class Controlador():
	def isIdle(self):
		return bool(random.randint(0,1))
		
	def hacerEfecto(self,idEfecto):
		print("[Mensaje del Controlador]: Despache un efecto a la nube")
		
#TODO: Cambiar esto por un map para contar notificaciones x red social
#Onda {''facebook': 5, 'twitter': 10}
acum = 0  #acumulacion


#Mapper
#Thread que esta corriendo continuamente y mapea acciones al Controlador
class Mapper(threading.Thread):  
	def __init__(self):  
		threading.Thread.__init__(self)  
		self.controlador = Controlador()

	def run(self):
		global acum
		while(True):
			if acum > 0:
				print "[Mensaje del Mapper]: Tengo ", acum, " notificaciones para procesar"
				if not self.controlador.isIdle():
					print "[Mensaje del Mapper]: El controlador ESTA disponible :)"
					acum = acum - 1
					self.controlador.hacerEfecto(400)
				else:
					print "[Mensaje del Mapper]: El controlador no esta disponible :("
			else:
				print "[Mensaje del Mapper]: Durmiendo... zzzzzZzzZzz"
			time.sleep(1)

#Rest
#Servidor Rest implementado con Flask
#No consegui (Mauro) hacer que corra en el hilo principal de forma correcta junto con el Mapper
#Tuve que ponerlo en otro thread separado
class Rest(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		app = Flask(__name__)
		
		app.config.update(dict(
			DEBUG=False, #Codear y debuggear sin necesidad de resetear la app
		))
		
		#Index de la app (http://localhost:5000)
		@app.route('/')
		def index():
			url_for('static', filename='nube_mapper.jpg');
			return render_template('index.html');

		@app.route('/<redsocial>/<evento>/<numero>', methods=['GET', 'POST'])
		def mapper(redsocial,evento,numero):
			global acum
			if numero:
				#TODO: Con acum una estructura tipo Map
				#Mapear la acumulacion por red social (y evento si se quiere)
				#las variables son redsocial y evento
				acum = acum + int(numero)
			return 'true';
		app.run()

mapper 	= Mapper();
rest 			= Rest();

if __name__ == "__main__":
	#TODO: Hacer q termine la ejecucion, tipo con CTRL + C
	rest.start()
	mapper.start()
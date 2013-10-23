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

filtroEventos = {'like':0, 'comment':0}  # acumulacion de eventos segun su tipo

def inicializarTablaEventos():
	
	return {'like':1 , 'comment':2, 'hashtag':3}

def hayEventosEn(filtroEventos):
	
	for x in filtroEventos:
		if (filtroEventos[x] > 0):
			return True
	return False

#Mapper
#Thread que esta corriendo continuamente y mapea acciones al Controlador
class Mapper(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.controlador = Controlador()

	def run(self):
		
		global filtroEventos
		
		tablaEventos = inicializarTablaEventos()
		cont = 0 # trabaja como iterador de la lista
		
		while(True):
			
			if (hayEventosEn(filtroEventos)) :  # solo entra SI HAY CANTIDAD distinta de cero
				
				listaEventos = filtroEventos.items() # lista DE TUPLAS con (clave, valor)
				
				print "[Mensaje del Mapper]: Tengo ", len(listaEventos), " notificaciones para procesar"
				
				if self.controlador.isIdle():
					print "[Mensaje del Mapper]: El controlador ESTA disponible :)"
					
					while (listaEventos[cont][1] == 0): #no infinito porque el if principal asegura que hay uno != 0
						cont+=1
						if cont >= len(listaEventos):
							cont = 0 
						
					evento = listaEventos[cont][0] #evento es el nombre del evento a enviar
					efectoAEnviar = tablaEventos[evento] #efectoAEnviar es el NUMERO designado para el evento
					
					self.controlador.hacerEfecto(efectoAEnviar)
					
					filtroEventos[evento] = 0 # reinicio contador de evento enviado
					
					cont += 1
					
					#para evitar ingresos invalidos reinicio contador
					if cont >= len(listaEventos):
						cont = 0
					
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
			global filtroEventos
			
			cant = int(numero) # por las dudas =)
			
			if filtroEventos.has_key(evento.lower()):
				
				
				#incremento la cant que tenia segun el num recibido
				filtroEventos[evento.lower()] = filtroEventos[evento.lower()] + cant
			
			else:
				#creo nuevo evento
				filtroEventos[evento.lower()] = cant
						
			return 'true';
			
		app.run()

mapper  = Mapper();
rest    = Rest();

if __name__ == "__main__":
	#TODO: Hacer q termine la ejecucion, tipo con CTRL + C
	rest.start()
	mapper.start()

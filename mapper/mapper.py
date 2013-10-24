from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash
import threading, time, signal, sys, random

#Controlador
class Controlador():
	def isIdle(self):
		return bool(random.randint(0,1))
	
	def hacerEfecto(self,idEfecto):
		if idEfecto != None:
			print("[Mensaje del Controlador]: Despache el efecto Id ", idEfecto ," a la nube")
                
filtroEventos = {} 

#Mapper
#Thread que esta corriendo continuamente y mapea acciones al Controlador
class Mapper(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.controlador = Controlador()
		
	def calcularEfecto(self, evento, cantidad):
		if evento == 'like':
			return 1
		if evento == 'comment':
			return 2
		if evento == 'hashtag':
			return 3
		if evento == 'mention
			return 4
		if evento == 'share'
			return 5
		return None
		
	def hayEventosEn(self, filtroEventos):
		for x in filtroEventos:
			if (filtroEventos[x] > 0):
				return True
		return False
		
	def run(self):
		global filtroEventos
		while(True):
			if (self.hayEventosEn(filtroEventos)) : 
				
				print "[Mensaje del Mapper]: Tengo notificaciones para procesar"
				
				for (evento,cantidad) in filtroEventos.items():
					if self.controlador.isIdle():
						print "[Mensaje del Mapper]: El controlador ESTA disponible :)"
						efectoAEnviar = self.calcularEfecto( evento, cantidad );
						self.controlador.hacerEfecto(efectoAEnviar)
						filtroEventos[evento] = 0
					else:
						print "[Mensaje del Mapper]: El controlador no esta disponible :("
			else:
				print "[Mensaje del Mapper]: Durmiendo... zzzzzZzzZzz"
					
			time.sleep(1)

#Rest
#Servidor Rest implementado con Flask
class Rest(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		app = Flask(__name__)
		
		app.config.update(dict(
			DEBUG=False, 
		))
		
		#Index de la app (http://localhost:5000)
		@app.route('/')
		def index():
			url_for('static', filename='nube_mapper.jpg');
			return render_template('index.html');
			
		@app.route('/<redsocial>/<evento>/<numero>', methods=['GET', 'POST'])
		def mapper(redsocial,evento,numero):
			global filtroEventos
			
			cant = int(numero) 
			
			if filtroEventos.has_key(evento.lower()):
				filtroEventos[evento.lower()] = filtroEventos[evento.lower()] + cant
			
			else:
				filtroEventos[evento.lower()] = cant
			return 'true';
			
		app.run()

mapper  	= Mapper();
rest    		= Rest();

if __name__ == "__main__":
	rest.start()
	mapper.start()
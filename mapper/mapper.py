from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

app.config.update(dict(
    DEBUG=True, #Codear y debuggear sin necesidad de resetear la app
))

#Index de la app (http://localhost:5000)
@app.route('/')
def index():
	url_for('static', filename='nube_mapper.jpg');
	return render_template('index.html');

@app.route('/facebook/<event>', methods=['GET', 'POST'])
def facebook(event):
	#TODO: Implementar logica de cada evento
	if event == 'like': 
		facebook_like();
		return 'true';
	if event == 'comment':
		facebook_comment();
		return 'true';
	return 'false';
	
def facebook_like():
	return;
	
def facebook_comment():
	return;
	
@app.route('/twitter/<event>', methods=['GET', 'POST'])
def twitter(event):
	#TODO: Implementar logica de cada evento
	if event == 'hashtag': 
		twitter_hashtag();
		return 'true';
	if event == 'mention':
		twitter_mention();
		return 'true';
	return 'false';
	
def twitter_hashtag():
	return;

def twitter_mention():
	return;
	
if __name__ == "__main__":
    app.run()
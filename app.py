from flask import Flask, render_template, request
from gtts import gTTS
import soundfile as sf
from numpy import *
from playsound import playsound
import random
import time
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import wave
#import playsound
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#/home/dhanno/Documents/flask/templates
UPLOAD_FOLDER = '/home/dhanno/Documents/flask/static'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #standard address for storing db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app) #initialize db
class User(db.Model):  # flask model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    soundfile = db.Column(db.String(180))  #will be storing audio files potentially
    
    def __repr__(self) -> str:
        return self.title
    
@app.route('//', methods=['POST', 'GET'])
def hello_world():
    
    if request.method == 'POST':
        text = request.form['text']
        language = 'en'       
        myobj = gTTS(text=text, lang=language, slow=False) #gTTs applied
        #myobj.save(f"/home/dhanno/Documents/flask/static/welcome{random.randint(0,99)}.wav")
        myobj.save(f"/home/dhanno/Documents/flask/static/welcome{text}.wav")
        playsound(f"/home/dhanno/Documents/flask/static/welcome{text}.wav")
        time.sleep(1)
        b = (f"/home/dhanno/Documents/flask/static/welcome{text}.wav")  #random array
        
        #string = ' '.join([str(elem) for elem in b]) # converted to array
        a_byte = bytearray(b, 'utf-32') # array converted to byte
        newtext = User(title=text, soundfile=b)
        #newtext = User(title=text)
        db.session.add(newtext)
        db.session.commit()     
        #os.system("/home/dhanno/Documents/flask/static//welcome1.mp3")
        return render_template("index.html")
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask, render_template, request
from gtts import gTTS
#import playsound
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
#/home/dhanno/Documents/flask/templates

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #standard address for storing db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #initialize db
class User(db.Model):  # flask model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    #soundfile = db.Column(db.LargeBinary)  #will be storing audio files potentially
    
    def __repr__(self) -> str:
        return self.title
    
    
@app.route('//', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        text = request.form['text']
        language = 'en'
        newtext = User(title=text)#text from input embedded to model
        db.session.add(newtext) # instance from model embedded to db     
        db.session.commit() 
        myobj = gTTS(text=text, lang=language, slow=False) #gTTs applied
        myobj.save("welcome1.mp3") # file saved
        os.system("/home/dhanno/Documents/flask/static//welcome1.mp3")
        return render_template("index.html")
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    

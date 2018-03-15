import os
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)



@app.route('/')
def madform():
    return render_template('form.html')

@app.route('/story.html', methods=['POST'])
def madstory():
    madwords = {
        'noun1' : request.form['noun1'],
        'noun2' : request.form['noun2'],
        'noun3' : request.form['noun3'],
        'noun4' : request.form['noun4'],
        'verb1' : request.form['verb1'],
        'verb2' : request.form['verb2'],
        'verb3' : request.form['verb3'],
        'verb4' : request.form['verb4'],
        'verb5' : request.form['verb5'],
        'verb6' : request.form['verb6'],
        'common_noun1' : request.form['common_noun1'],
        'common_noun2' : request.form['common_noun2'],
        'adverb1' : request.form['adverb1'],
        
    }
    return render_template('story.html', madwords = madwords)
    

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port = port, host = host)
    
    # local porting info etc
# Python para Web
# Python é uma linguagem de programação de uso geral e pode ser usada em muitos lugares. 
# Existem muitos trabalhos em web frames em Python. 
# Django e Flask são os mais populares. Veremos como usar o Flask para desenvolvimento web.


#Flask
# Flask é uma estrutura de desenvolvimento web escrita em Python. Flask usa mecanismo de modelo Jinja2. 
# O Flask também pode ser usado com outras bibliotecas frontais modernas, como React.

# let's import the flask
# let's import the flask
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
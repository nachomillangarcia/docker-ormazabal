# flask_web/app.py
import sys
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Leer variables de entorno
    foo = os.getenv('FOO', "DEFAULT")

    return f'''Hey, we have Flask in a Docker container!!!! 
    <br> envvar: {foo} 
    '''

app.run(debug=True, host='0.0.0.0')
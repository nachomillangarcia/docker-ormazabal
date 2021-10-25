# flask_web/app.py
import sys
import os
from flask import Flask

import config as cfg

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Leer variables de entorno
    foo = os.getenv('FOO', "DEFAULT")

    # Leer archivo configuracion
    password = cfg.password

    # Leer argumentos linea de comandos
    args = str(sys.argv)

    return f'''Hey, we have Flask in a Docker container!!!! 
    <br> envvar: {foo} 
    <br> password: {password}
    <br> arguments: {args}
    
    '''

app.run(debug=True, host='0.0.0.0')
# flask_web/app.py
import sys
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    return f'''Hey, we have Flask in a Docker container!!!! '''

app.run(debug=True, host='0.0.0.0')
# 플라스크 웹 서버
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/') # http://localhost:5000/

def index():
    return 'Hello, Flask!!'

if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)
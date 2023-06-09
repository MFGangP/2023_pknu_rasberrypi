# 플라스크 웹 서버
import sys
from flask import Flask, render_template

app = Flask(__name__)
# 경로를 변경하는 방법
@app.route('/hello') # http://localhost:8000/hello

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)
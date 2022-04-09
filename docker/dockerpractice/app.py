from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print ('Web App with Python Flask! \n Hello World \n By {}'.format(os.environ.get('MY_NAME')))
    return '<h1>Web App with Python Flask!</h1> <br> Hello World <br> By {}'.format(os.environ.get('MY_NAME'))

app.run(host='0.0.0.0', port=81, debug=True)
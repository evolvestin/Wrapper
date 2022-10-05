import _thread
from time import sleep
from flask import Flask
app = Flask(__name__)


def herl():
    count = 0
    while True:
        count += 1
        print('привет', count)
        sleep(5)


@app.route('/')
def hello_world():
    _thread.start_new_thread(herl, ())
    return 'Hello, World!'

# app.run(host='0.0.0.0', port='5000', debug=True)

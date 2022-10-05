import _thread
import os
from time import sleep
from flask import Flask
app = Flask(__name__)


def herl():
    from telebot import TeleBot
    count = 0
    bot = TeleBot(os.environ['go'])
    while True:
        count += 1
        bot.send_message(396978030, f'привет {count}')
        print('привет', count)
        sleep(5)


@app.route('/')
def hello_world():
    _thread.start_new_thread(herl, ())
    return 'Hello, World!'


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()

# app.run(host='0.0.0.0', port='5000', debug=True)

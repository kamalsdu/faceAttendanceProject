from flask import Flask
import requests

APP = Flask(__name__)


@APP.route('/')
def hello_world():
    # files = {
    #     'photo[0] ': (None, '@/home/kamalkhan/Desktop/img1.jpg'),
    #     'photo[1] ': (None, '@/home/kamalkhan/Desktop/img1.jpg'),
    # }
    #
    # response = requests.post('https://verigram.kz/api/', files=files)
    # print(response.content)
    return 'Hello'


if __name__ == '__main__':
    APP.run()

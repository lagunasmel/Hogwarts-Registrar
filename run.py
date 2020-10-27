from flask import Flask

hogwarts = Flask(__name__)


@hogwarts.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    hogwarts.run()
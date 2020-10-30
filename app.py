from flask import Flask, render_template

hogwarts = Flask(__name__)


@hogwarts.route('/test')
def hello_world():
    return 'Hello World!'


@hogwarts.route('/')
def index():
    return render_template('index.html')


@hogwarts.route('/students')
def students():
    return render_template('content.html')


@hogwarts.route('/instructors')
def instructors():
    return render_template('content.html')


@hogwarts.route('/classes')
def classes():
    return render_template('content.html')


@hogwarts.route('/houses')
def houses():
    return render_template('content.html')


@hogwarts.route('/enrollments')
def enrollments():
    return render_template('content.html')


if __name__ == '__main__':
    hogwarts.run()

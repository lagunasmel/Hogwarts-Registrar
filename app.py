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
    data = {'title': "Students"}
    return render_template('students.html', data=data)


@hogwarts.route('/instructors')
def instructors():
    data = {'title': "Instructors"}
    return render_template('content.html', data=data)


@hogwarts.route('/classes')
def classes():
    data = {'title': "Classes"}
    return render_template('content.html', data=data)


@hogwarts.route('/houses')
def houses():
    data = {'title': "Houses"}
    return render_template('content.html', data=data)


@hogwarts.route('/enrollments')
def enrollments():
    data = {'title': "Enrollments"}
    return render_template('content.html', data=data)


if __name__ == '__main__':
    hogwarts.run()

from flask import Flask, render_template

hogwarts = Flask(__name__)


@hogwarts.route('/test')
def hello_world():
    return 'Hello World!'


@hogwarts.route('/')
def index():
    return render_template('index.html', posts=posts)


@hogwarts.route('/students')
def students():
    data = {'title': "Students"}
    form_inputs = [
        {"name": "name", "placeholder": "Name of Student?"},
        {"name": "houseName", "placeholder": "Name of House?"},
        {"name": "year", "type": "number", "placeholder": "Year of Student?"},
        {"name": "prefect", "type": "checkbox", "label": "Is student a prefect?"},
        {"name": "submit", "type": "button", "value": "Add Student"}
    ]
    data['inputs'] = form_inputs
    table = {
        "caption": "Student Data",
        "headers": ["Student Name", "House Name", "Year", "Prefect?"],
        "rows": [
            ["Hermione", "Gryffindor", "5", "No"]
        ]
    }
    data['table'] = table
    return render_template('content.html', data=data)


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
    hogwarts.run(debug=True)

from flask import Flask, render_template
import os
import urllib
import mysql.connector

# DB info and example connection
db_url = os.getenv('DATABASE_URL')
db_info = urllib.parse.urlparse(db_url)
mydb = mysql.connector.connect(host=db_info.hostname, user=db_info.username, password=db_info.password)
c = mydb.cursor()
db_name = db_info.path[1:]
c.execute(f'USE {db_name}')
c.execute("SELECT * FROM houses;")
mydb.close()

hogwarts = Flask(__name__)


@hogwarts.route('/')
def index():
    return render_template('index.html')


# Current students route for now!
@hogwarts.route('/students')
def students():
    data = {'title': "Students"}
    table = {
        "caption": "Student Data",
        "headers": ["Student Name", "House Name", "Year", "Prefect?"],
        "rows": [
            ["Hermione", "Gryffindor", "5", "No"]
        ]
    }
    data['table'] = table
    data['housenames'] = [(1, 'NULL'), (2, 'House1')]
    return render_template('students.html', data=data)


@hogwarts.route('/instructors')
def instructors():
    data = {'title': "Instructors"}
    table = {
        "caption": "Instructor Data",
        "headers": ["Instructor Name", "House Name"],
        "rows": [
            ["Minerva McGonagall", "Gryffindor"]
        ]
    }
    data['table'] = table
    return render_template('instructors.html', data=data)


@hogwarts.route('/classes')
def classes():
    data = {'title': "Classes"}
    table = {
        "caption": "Classes Data",
        "headers": ["Class Name", "Instructor Name", "Max Size"],
        "rows": [
            ["Advanced Potions", "Severus Snape", "25"]
        ]
    }
    data['table'] = table
    return render_template('classes.html', data=data)


@hogwarts.route('/houses')
def houses():
    data = {'title': "Houses"}
    table = {
        "caption": "Houses Data",
        "headers": ["House Name", "Founder Name", "House Animal", "Number of Points"],
        "rows": [
            ["Gryffindor", "Godric Gryffindor", "Lion", "25"]
        ]
    }
    data['table'] = table
    return render_template('houses.html', data=data)


@hogwarts.route('/enrollments')
def enrollments():
    data = {'title': "Enrollments"}
    table = {
        "caption": "Student Enrollment Data",
        "headers": ["Student Name", "Class Name", "Finished?", "Rating"],
        "rows": [
            ["Hermione Granger", "Advanced Potions", "No", "N/A"]
        ]
    }
    data['table'] = table
    return render_template('enrollments.html', data=data)


if __name__ == '__main__':
    hogwarts.run(debug=True)

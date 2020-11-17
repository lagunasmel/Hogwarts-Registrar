from flask import Flask, render_template, g
import os
import urllib
import mysql.connector

"""
# DB info and example connection
db_url = os.getenv('DATABASE_URL')
db_info = urllib.parse.urlparse(db_url)
mydb = mysql.connector.connect(host=db_info.hostname, user=db_info.username, password=db_info.password)
c = mydb.cursor()
db_name = db_info.path[1:]
c.execute(f'USE {db_name}')
c.execute("SELECT * FROM Houses;")
mydb.close()
"""

hogwarts = Flask(__name__)


# Auto-closes db connection at the end of each request
@hogwarts.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_db():
    """Opens a new db connection or returns the existing one"""
    db = getattr(g, '_database', None)
    if db is None:
        db_url = os.getenv('DATABASE_URL')
        db_info = urllib.parse.urlparse(db_url)
        db = g._database = mysql.connector.connect(host=db_info.hostname, user=db_info.username,
                                                   password=db_info.password)
        c = db.cursor()
        db_name = db_info.path[1:]
        c.execute(f'USE {db_name}')
    return db


@hogwarts.route('/')
def index():
    return render_template('index.html')


# Current students route for now!
@hogwarts.route('/students')
def students():
    data = {'title': "Students"}
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute(
        """SELECT s.studentID, s.name studentName, h.name houseName, s.year, s.prefect, s.patronus, s.wandType FROM 
        Students AS s 
        INNER JOIN Houses AS h 
        ON s.houseID = h.houseID;""")
    rows = c.fetchall()

    table = {
        "caption": "Student Data",
        "headers": ["Student Name", "House Name", "Year", "Prefect?", "Patronus", "Wand Type"],
        "columns": ['studentName', 'houseName', 'year', 'prefect', 'patronus', 'wandType'],
        "id_col_name": 'studentID',
        "rows": rows
    }
    data['table'] = table
    c.execute("""SELECT houseId, name FROM Houses;""")
    rows = c.fetchall()
    housenames = [(row['houseId'], row['name']) for row in rows]
    data['housenames'] = housenames
    return render_template('students.html', data=data)


@hogwarts.route('/instructors')
def instructors():
    data = {'title': "Instructors"}
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute(
        """SELECT i.instructorID, i.name instructorName, h.name houseName, i.patronus, i.wandType
            FROM Instructors AS i
            INNER JOIN Houses AS h on i.houseID = h.houseID;""")
    rows = c.fetchall()

    table = {
        "caption": "Instructor Data",
        "headers": ["Instructor Name", "House Name", "Patronus", "Wand Type"],
        "columns": ['instructorName', 'houseName', 'patronus', 'wandType'],
        "id_col_name": 'instructorID',
        "rows": rows
    }
    data['table'] = table
    c.execute("""SELECT houseId, name FROM Houses;""")
    rows = c.fetchall()
    housenames = [(row['houseId'], row['name']) for row in rows]
    data['housenames'] = housenames

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

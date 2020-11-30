from flask import Flask, render_template, g, flash
from flask import request as req
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

hogwarts.config['SECRET_KEY'] = 't62hMWeN4sV54A5e'


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
def students(search_str=None):
    data = {'title': "Students"}
    db = get_db()
    c = db.cursor(dictionary=True)
    if search_str is None:
        c.execute(
            """SELECT s.studentID, s.name studentName, h.name houseName, s.year, s.prefect, s.patronus, s.wandType FROM 
            Students AS s 
            INNER JOIN Houses AS h 
            ON s.houseID = h.houseID;""")
    else:
        search_str = '%' + search_str + '%'
        c.execute(
            """SELECT s.studentID, s.name studentName, h.name houseName, s.year, s.prefect, s.patronus, s.wandType FROM 
            Students AS s 
            INNER JOIN Houses AS h 
            ON s.houseID = h.houseID
            WHERE s.name LIKE %s;""", (search_str,))
    rows = c.fetchall()

    for row in rows:
        if row['prefect'] == 0:
            row['prefect'] = 'False'
        else:
            row['prefect'] = 'True'

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


@hogwarts.route('/_search-students', methods=['POST'])
def search_students():
    request = req.get_json()
    db = get_db()
    c = db.cursor(dictionary=True)
    data = request['data']
    search_str = data['name']
    if search_str == "":
        search_str = None
    return students(search_str)


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
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute(
        """SELECT c.classID, c.name className, i.name instructorName, c.maxSize, c.description
            FROM Classes AS c
            INNER JOIN Instructors i on c.instructorID = i.instructorID;""")
    rows = c.fetchall()

    table = {
        "caption": "Classes Data",
        "headers": ["Class Name", "Instructor Name", "Max Size", "Description"],
        "columns": ['className', 'instructorName', 'maxSize', 'description'],
        "id_col_name": 'classID',
        "rows": rows
    }
    data['table'] = table
    c.execute("""SELECT instructorID, name FROM Instructors;""")
    rows = c.fetchall()
    instructornames = [(row['instructorID'], row['name']) for row in rows]
    data['instructornames'] = instructornames
    return render_template('classes.html', data=data)


@hogwarts.route('/houses')
def houses():
    data = {'title': "Houses"}
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute(
        """SELECT houseID, name, founder, animal, colors, points
            FROM Houses;""")
    rows = c.fetchall()

    table = {
        "caption": "Houses Data",
        "headers": ["House Name", "Founder", "House Animal", "House Colors", "Points"],
        "columns": ['name', 'founder', 'animal', 'colors', 'points'],
        "id_col_name": 'houseID',
        "rows": rows
    }
    data['table'] = table
    return render_template('houses.html', data=data)


@hogwarts.route('/enrollments')
def enrollments():
    data = {'title': "Enrollments"}
    db = get_db()
    c = db.cursor(dictionary=True)
    c.execute(
        """SELECT sce.enrollmentID, s.name studentName, c.name className, sce.finished, sce.rating, sce.year, sce.term
            FROM StudentClassEnrollments AS sce
            INNER JOIN Students AS s ON sce.studentID = s.studentID
            INNER JOIN Classes AS c ON sce.classID = c.classID;""")
    rows = c.fetchall()

    for row in rows:
        if row['finished'] == 0:
            row['finished'] = 'False'
        else:
            row['finished'] = 'True'

    table = {
        "caption": "Enrollments Data",
        "headers": ["Student Name", "Class Name", "Finished?", "Rating", "Year", "Term"],
        "columns": ['studentName', 'className', 'finished', 'rating', 'year', 'term'],
        "id_col_name": 'enrollmentID',
        "rows": rows
    }
    data['table'] = table
    c.execute("""SELECT classID, name FROM Classes;""")
    rows = c.fetchall()
    classnames = [(row['classID'], row['name']) for row in rows]
    data['classnames'] = classnames
    return render_template('enrollments.html', data=data)


@hogwarts.route('/_insert-row', methods=['POST'])
def insert_row():
    request = req.get_json()
    db = get_db()
    c = db.cursor(dictionary=True)
    if request['tableName'] == 'Students':
        data = request['data']
        c.execute("""INSERT INTO Students(name, year, patronus, wandType, prefect, houseID)
                        VALUES (%s, %s, %s, %s, %s, %s);""",
                  (data['name'], data['year'], data['patronus'], data['wandType'], data['prefect'], data['houseID']))
        db.commit()
        return students()
    elif request['tableName'] == 'Instructors':
        data = request['data']
        if data['houseID'] == '0':
            data['houseID'] = None
        c.execute("""INSERT INTO Instructors(name, patronus, wandType, houseID)
                                VALUES (%s, %s, %s, %s);""",
                  (data['name'], data['patronus'], data['wandType'], data['houseID']))
        db.commit()
        return instructors()
    elif request['tableName'] == 'Classes':
        data = request['data']
        instructor_id = data['instructor']
        c.execute("""INSERT INTO Classes(name, maxSize, description, instructorID)
                                        VALUES (%s, %s, %s, %s);""",
                  (data['name'], data['size'], data['description'], instructor_id))
        db.commit()
        return classes()
    elif request['tableName'] == 'Houses':
        data = request['data']
        c.execute("""INSERT INTO Houses(name, founder, animal, colors, points)
                                        VALUES (%s, %s, %s, %s, %s);""",
                  (data['name'], data['founder'], data['animal'], data['colors'], data['points']))
        db.commit()
        return houses()
    elif request['tableName'] == 'StudentClassEnrollments':
        data = request['data']
        # First get the student and class IDs
        c.execute("""SELECT studentID FROM Students WHERE name = %s;""", (data['name'],))
        student_rows = c.fetchall()
        if len(student_rows) == 0:
            return enrollments()
        student_id = student_rows[0]['studentID']
        class_id = data['class']
        # Clean the other data
        if data['rating'] == "":
            data['rating'] = None
        c.execute("""INSERT INTO StudentClassEnrollments(studentID, classID, finished, rating, year, term)
                                                VALUES (%s, %s, %s, %s, %s, %s);""",
                  (student_id, class_id, data['finished'], data['rating'], data['year'], data['term']))
        db.commit()
        return enrollments()


@hogwarts.route('/_delete-row', methods=['POST'])
def delete_row():
    request = req.get_json()
    row_id = request['rowId']
    db = get_db()
    c = db.cursor(dictionary=True)
    if request['tableName'] == 'Students':
        try:
            c.execute("""DELETE
                            FROM Students
                            WHERE studentID = %s;""", (row_id,))
        except:
            flash('This Student could not be deleted.'
                  ' Please remove Student from Enrollments prior to deletion attempts.')

        db.commit()
        return students()

    elif request['tableName'] == 'Instructors':
        try:
            c.execute("""DELETE FROM Instructors WHERE instructorID = %s;""", (row_id,))
        except:
            flash('This Instructor could not be deleted.'
                  ' Please remove Instructor from Classes prior to deletion attempts.')

        db.commit()
        return instructors()
    elif request['tableName'] == 'Classes':
        c.execute("""DELETE FROM Classes WHERE classID = %s;""", (row_id,))
        db.commit()
        return classes()
    elif request['tableName'] == 'Houses':
        c.execute("""DELETE FROM Houses WHERE houseID = %s;""", (row_id,))
        db.commit()
        return houses()
    elif request['tableName'] == 'StudentClassEnrollments':
        c.execute("""DELETE FROM StudentClassEnrollments WHERE enrollmentID = %s;""", (row_id,))
        db.commit()
        return enrollments()


@hogwarts.route('/_update-row', methods=['POST'])
def update_row():
    request = req.get_json()
    db = get_db()
    c = db.cursor(dictionary=True)
    if request['tableName'] == 'Houses':
        data = request['data']
        c.execute("""UPDATE Houses SET name=%s, founder=%s, animal=%s, colors=%s, points=%s
        WHERE houseID=%s;""", (
            data['newName'], data['newFounder'], data['newAnimal'], data['newColors'], data['newPoints'],
            data['houseID']))
        db.commit()
        return houses()


if __name__ == '__main__':
    hogwarts.run(debug=True)

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS houses;


CREATE TABLE houses (
    houseID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    founder VARCHAR(255) NOT NULL,
    animal VARCHAR (255) NOT NULL,
    colors VARCHAR(255) NOT NULL,
    points INT(11) NOT NULL DEFAULT 0
);

CREATE TABLE students (
    studentID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    year INT(4) NOT NULL,
    patronus VARCHAR (250),
    wandType VARCHAR(250),
    prefect BOOLEAN not NULL DEFAULT FALSE,
    houseID INT NOT NULL DEFAULT 0,
    FOREIGN KEY (houseID) REFERENCES houses(houseID)
);

CREATE TABLE instructors (
    instructorID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    patronus VARCHAR (250),
    wandType VARCHAR(250),
    houseID INT NOT NULL,
    FOREIGN KEY (houseID) REFERENCES houses(houseID)
);

CREATE TABLE classes (
    classID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    maxSize INT(11) NOT NULL DEFAULT 0,
    description VARCHAR(255),
    instructorID INT NOT NULL,
    FOREIGN KEY (instructorID) REFERENCES instructors(instructorID)
);

-- House Data
INSERT INTO houses (name, founder, animal, colors)
VALUES('Gryffindor', 'Godric Gryffindor', 'Lion', 'Red and Gold');

INSERT INTO houses (name, founder, animal, colors)
VALUES('Ravenclaw', 'Rowena Ravenclaw', 'Eagle', 'Blue and Bronze');

INSERT INTO houses (name, founder, animal, colors)
VALUES('Slytherin', 'Salazar Slytherin', 'Snake', 'Green and Silver');

INSERT INTO houses (name, founder, animal, colors)
VALUES('Hufflepuff', 'Helga Hufflepuff', 'Badger', 'Yellow and Black');



INSERT INTO students (name, year, patronus, wandType, prefect, houseID)
VALUES('Harry Potter', 1, 'Stag', 'Elder Wood', FALSE, (SELECT houseID FROM houses WHERE name='Gryffindor'));

select * from students;
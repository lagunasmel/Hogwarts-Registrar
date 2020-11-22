DROP TABLE IF EXISTS StudentClassEnrollments;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Houses;


CREATE TABLE Houses
(
    houseID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name    VARCHAR(255)                  NOT NULL,
    founder VARCHAR(255)                  NOT NULL,
    animal  VARCHAR(255)                  NOT NULL,
    colors  VARCHAR(255)                  NOT NULL,
    points  INT(11)                       NOT NULL DEFAULT 0
);

CREATE TABLE Students
(
    studentID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name      VARCHAR(250)                  NOT NULL,
    year      INT(4)                        NOT NULL,
    patronus  VARCHAR(250),
    wandType  VARCHAR(250),
    prefect   BOOLEAN                       not NULL DEFAULT FALSE,
    houseID   INT                           NOT NULL DEFAULT 0,
    FOREIGN KEY (houseID) REFERENCES Houses (houseID)
);

CREATE TABLE Instructors
(
    instructorID INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name         VARCHAR(250)                  NOT NULL,
    patronus     VARCHAR(250),
    wandType     VARCHAR(250),
    houseID      INT,
    FOREIGN KEY (houseID) REFERENCES Houses (houseID)
);

CREATE TABLE Classes
(
    classID      INT(11) UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name         VARCHAR(255)                  NOT NULL,
    maxSize      INT(11)                       NOT NULL DEFAULT 0,
    description  VARCHAR(255),
    instructorID INT                           NOT NULL,
    FOREIGN KEY (instructorID) REFERENCES Instructors (instructorID)
);

CREATE TABLE StudentClassEnrollments
(
    enrollmentID INT(11) AUTO_INCREMENT NOT NULL,
    studentID    INT(11)                NOT NULL,
    classID      INT(11)                NOT NULL,
    finished     BOOLEAN                NOT NULL,
    rating       INT(11),
    year         INT(11)                NOT NULL,
    term         INT(11),
    PRIMARY KEY (enrollmentID),
    FOREIGN KEY (studentID) REFERENCES Students (studentID),
    FOREIGN KEY (classID) REFERENCES Classes (classID)
);

-- House Data
INSERT INTO Houses (name, founder, animal, colors)
VALUES ('Gryffindor', 'Godric Gryffindor', 'Lion', 'Red and Gold'),
       ('Ravenclaw', 'Rowena Ravenclaw', 'Eagle', 'Blue and Bronze'),
       ('Slytherin', 'Salazar Slytherin', 'Snake', 'Green and Silver'),
       ('Hufflepuff', 'Helga Hufflepuff', 'Badger', 'Yellow and Black');

INSERT INTO Students (name, year, patronus, wandType, prefect, houseID)
VALUES ('Harry Potter', 1, 'Stag', 'Elder Wood', FALSE, (SELECT houseID FROM Houses WHERE name = 'Gryffindor')),
       ('Hermione Granger', 1, 'Otter', 'Vine Wood', FALSE, (SELECT houseID FROM Houses WHERE name = 'Gryffindor')),
       ('Draco Malfoy', 1, NULL, 'Hawthorn Wood', FALSE, (SELECT houseID FROM Houses WHERE name = 'Slytherin')),
       ('Percy Weasley', 4, NULL, 'Wood', TRUE, (SELECT houseID FROM Houses WHERE name = 'Gryffindor')),
       ('Luna Lovegood', 1, 'Hare', 'Wood', FALSE, (SELECT houseID FROM Houses WHERE name = 'Hufflepuff'));

INSERT INTO Instructors (name, patronus, wandType, houseID)
VALUES ('Minerva McGonagall', 'Cat', 'Fir', (SELECT houseID FROM Houses WHERE name = 'Gryffindor')),
       ('Severus Snape', 'Doe', 'Wood', (SELECT houseID FROM Houses WHERE name = 'Slytherin')),
       ('Filius Flitwick', NULL, 'Wood', (SELECT houseID FROM Houses WHERE name = 'Ravenclaw'));

INSERT INTO Classes (name, maxSize, description, instructorID)
VALUES ('Transfiguration', 40, 'Alteration of the form or appearance of an object',
        (SELECT instructorID FROM Instructors WHERE name = 'Minerva McGonagall')),
       ('Potions', 20, 'The correct way to brew potions',
        (SELECT instructorID FROM Instructors WHERE name = 'Severus Snape')),
       ('Charms', 30, 'The science of charm-work',
        (SELECT instructorID FROM Instructors WHERE name = 'Filius Flitwick'));

INSERT INTO StudentClassEnrollments (studentID, classID, finished, rating, year, term)
VALUES ((SELECT studentID FROM Students WHERE name = 'Harry Potter'),
        (SELECT classID FROM Classes WHERE name = 'Transfiguration'), FALSE, NULL, 1, 1),
       ((SELECT studentID FROM Students WHERE name = 'Percy Weasley'),
        (SELECT classID FROM Classes WHERE name = 'Transfiguration'), TRUE, 8, 1, 1),
       ((SELECT studentID FROM Students WHERE name = 'Hermione Granger'),
        (SELECT classID FROM Classes WHERE name = 'Potions'), FALSE, NULL, 1, 1),
       ((SELECT studentID FROM Students WHERE name = 'Luna Lovegood'),
        (SELECT classID FROM Classes WHERE name = 'Charms'), FALSE, NULL, 1, 1);

select *
from Students;
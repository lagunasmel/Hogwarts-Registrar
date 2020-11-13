# Sample DMQs covering all functionality of our website
# ':' character denotes the variables that will have data from the backend programming language

# Add a student
INSERT INTO Students (name, year, patronus, wandType, prefect, houseID)
VALUES (:nameInput, :yearInput, :patronusInput, :wandInput, :prefectInput,
        :houseIDInput);

# Search student by name (select)
SELECT s.name, h.name, s.year, s.prefect
FROM Students AS s
         INNER JOIN Houses AS h ON s.houseID = h.houseID
WHERE s.name LIKE :filter;

# Update a student row
UPDATE Students
SET name     = :newName,
    year     = :newYear,
    patronus = :newPatronus,
    wandType = :newWandType,
    prefect  = :newPrefect,
    houseID  = :newHouseID
WHERE studentID = :chosenStudentID;

# Delete a student row
DELETE
FROM Students
WHERE studentID = :chosenStudentID;

# Add an instructor
INSERT INTO Instructors (name, patronus, wandType, houseID)
VALUES (:nameInput, :patronusInput, :wandInput, :houseIDInput);

# Select all instructor rows
SELECT i.name, h.name, i.patronus, i.wandType
FROM Instructors AS i
         INNER JOIN Houses AS h on i.houseID = h.houseID;

# Update an instructor row
UPDATE Instructors
SET name     = :newName,
    patronus = :newPatronus,
    wandType = :newWandType,
    houseID  = :newHouseID
WHERE instructorID = :chosenInstructorID;

# Delete an instructor row
DELETE
FROM Instructors
WHERE instructorID = :chosenInstructorID;

# Add a class
INSERT INTO Classes (name, maxSize, description, instructorID)
VALUES (:nameInput, :maxSizeInput, :descriptionInput, :instructorIDInput);

# Select all class rows
SELECT c.name, i.name, c.maxSize, c.description
FROM Classes AS c
         INNER JOIN Instructors i on c.instructorID = i.instructorID;

# Update a class row
UPDATE Classes
SET name         = :newName,
    maxSize      = :newMaxSize,
    description  = :newDescription,
    instructorID = :newInstructorID
WHERE classID = :chosenClassID;

# Delete a class row
DELETE
FROM Classes
WHERE classID = :chosenClassID;

# Add a house
INSERT INTO Houses (name, founder, animal, colors, points)
VALUES (:nameInput, :founderInput, :animalInput, :colorsInput, :pointsInput);

# Select all house rows
SELECT name, founder, animal, colors, points
FROM Houses;

# Update a house row
UPDATE Houses
SET name    = :newName,
    founder = :newFounder,
    animal  = :newAnimal,
    colors  = :newColors,
    points  = :newPoints
WHERE houseID = :chosenHouseID;

# Delete a house row
DELETE
FROM Houses
WHERE houseID = :chosenHouseID;

# Add an enrollment
INSERT INTO StudentClassEnrollments (studentID, classID, finished, rating, year, term)
VALUES (:studentIDInput, :classIDInput, :finishedInput, :ratingInput, :yearInput, :termInput);

# Select all enrollments
SELECT s.name, c.name, sce.finished, sce.rating, sce.year, sce.term
FROM StudentClassEnrollments AS sce
         INNER JOIN Students AS s ON sce.studentID = s.studentID
         INNER JOIN Classes AS c ON sce.classID = c.classID;

# Update an enrollment row
UPDATE StudentClassEnrollments
SET studentID = :newStudentID,
    classID   = :newClassID,
    finished  = :newFinished,
    rating    = :newRating,
    year      = :newYear,
    term      = :newTerm
WHERE studentID = :chosenStudentID
  AND classID = :chosenClassID;

# Delete an enrollment row
DELETE
FROM StudentClassEnrollments
WHERE studentID = :chosenStudentID
  AND classID = :chosenClassID;
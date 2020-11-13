# Sample DMQs covering all functionality of our website
# ':' character denotes the variables that will have data from the backend programming language

# Add a student
INSERT INTO Students (name, year, patronus, wandType, prefect, houseID)
VALUES (:nameInput, :yearInput, :patronusInput, :wandInput, :prefectInput,
        (SELECT houseID FROM Houses WHERE name = :houseNameInput));

# Search student by name (select)


# Update a student row

# Delete a student row

# Add an instructor

# Select all instructor rows

# Update an instructor row

# Delete an instructor row

# Add a class

# Select all class rows

# Update a class row

# Delete a class row

# Add a house

# Select all house rows

# Update a house row

# Delete a house row

# Add an enrollment

# Update an enrollment row

# Delete an enrollment row
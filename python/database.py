import json
import sqlite3

# Create a new database connection
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

# Insert records into the table
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('John Doe', 35))
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Jane Smith', 28))

# Commit the changes
conn.commit()

# Extract the data from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Convert the data to JSON format
data = []
for row in rows:
    data.append({'id': row[0], 'name': row[1], 'age': row[2]})
json_data = json.dumps(data, indent=4)

# Print the JSON data
print(json_data)

# Close the database connection
conn.close()

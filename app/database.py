import json
import sqlite3

# Create a new database connection

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')     
        print("Connected to the database")
    except sqlite3.Error as e:
        print(e)
    
    return conn

# Create a table
def insert_record(conn, record):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
    
    sql = "INSERT INTO employees (name, age) VALUES (?, ?)"
    cursor.execute(sql, record)
    conn.commit()
    print("Record inserted successfully")



def extract_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    data = []
    for row in rows:
        record = {'name': row[1], 'age': row[2]}
        data.append(record)
    json_data = json.dumps(data, indent=4)

    return json_data

# Main program
conn = create_connection()

# Insert records into the database
record1 = ('John Doe', 30)
record2 = ('Jane Smith', 25)

insert_record(conn, record1)
insert_record(conn, record2)

# Extract data from the database and convert to JSON
# data = extract_data(conn)
# json_data = convert_to_json(data)
# print(data)

# Close the database connection
conn.close()

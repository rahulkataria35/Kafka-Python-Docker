import json
import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        print("Connected to the database")
    except sqlite3.Error as e:
        print(e)
    
    return conn

def insert_record(conn, record):
    sql = '''INSERT INTO records(name, age, email) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()
    print("Record inserted successfully")

def extract_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM records")
    rows = cur.fetchall()

    data = []
    for row in rows:
        record = {'name': row[0], 'age': row[1], 'email': row[2]}
        data.append(record)

    return data

def convert_to_json(data):
    json_data = json.dumps(data)
    return json_data

# Main program
conn = create_connection()

# Insert records into the database
record1 = ('John Doe', 30, 'johndoe@example.com')
record2 = ('Jane Smith', 25, 'janesmith@example.com')

insert_record(conn, record1)
insert_record(conn, record2)

# Extract data from the database and convert to JSON
data = extract_data(conn)
json_data = convert_to_json(data)
print(json_data)

# Close the database connection
conn.close()

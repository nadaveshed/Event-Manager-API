import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)

# Create a cursor object
mycursor = mydb.cursor()


# Functions for database operations
def insert_event(event_data):
    sql = "INSERT INTO events (name, location, date, participants) VALUES (%s, %s, %s, %s)"
    values = (event_data['name'], event_data['location'], event_data['date'], event_data['participants'])
    mycursor.execute(sql, values)
    mydb.commit()


def get_events_by_location_or_venue(location):
    sql = "SELECT * FROM events WHERE location = %s"
    mycursor.execute(sql, (location,))
    return mycursor.fetchall()


def sort_events(sort_by):
    if sort_by == 'date':
        sql = "SELECT * FROM events ORDER BY date"
    elif sort_by == 'popularity':
        sql = "SELECT * FROM events ORDER BY participants DESC"
    elif sort_by == 'creation_time':
        sql = "SELECT * FROM events ORDER BY created_at DESC"
    mycursor.execute(sql)
    return mycursor.fetchall()

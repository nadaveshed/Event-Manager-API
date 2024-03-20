from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
auth = HTTPBasicAuth()

# Basic auth configuration
users = {
    "user": generate_password_hash("password")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)
mycursor = mydb.cursor()


# API endpoints
@app.route('/events', methods=['GET'])
@auth.login_required
def get_all_events():
    mycursor.execute("SELECT * FROM events")
    events = mycursor.fetchall()
    return jsonify(events)


@app.route('/events/<int:event_id>', methods=['GET'])
@auth.login_required
def get_event(event_id):
    mycursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
    event = mycursor.fetchone()
    if event:
        return jsonify(event)
    else:
        return jsonify({"error": "Event not found"}), 404


@app.route('/events', methods=['POST'])
@auth.login_required
def schedule_event():
    data = request.json
    sql = "INSERT INTO events (name, location, date, participants) VALUES (%s, %s, %s, %s)"
    values = (data['name'], data['location'], data['date'], data['participants'])
    mycursor.execute(sql, values)
    mydb.commit()
    return jsonify({"message": "Event scheduled successfully"})


@app.route('/events/<int:event_id>', methods=['PUT'])
@auth.login_required
def update_event(event_id):
    data = request.json
    sql = "UPDATE events SET name = %s, location = %s, date = %s, participants = %s WHERE id = %s"
    values = (data['name'], data['location'], data['date'], data['participants'], event_id)
    mycursor.execute(sql, values)
    mydb.commit()
    return jsonify({"message": f"Event {event_id} updated successfully"})


@app.route('/events/<int:event_id>', methods=['DELETE'])
@auth.login_required
def delete_event(event_id):
    sql = "DELETE FROM events WHERE id = %s"
    mycursor.execute(sql, (event_id,))
    mydb.commit()
    return jsonify({"message": f"Event {event_id} deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)

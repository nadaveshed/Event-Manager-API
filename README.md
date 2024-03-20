# Event Manager API

The Event Manager API is a Flask-based RESTful API that allows users to schedule, retrieve, update, and delete events. It provides endpoints for managing events stored in a MySQL database. This README provides instructions on setting up the project, creating the required database table, and using the API endpoints.

## Setup

1. Clone the repository:

git clone https://github.com/yourusername/event-manager-api.git


2. Install the needed dependencies


3. Start the Flask application:

```python app.py```

## Database Setup

Before using the API, you need to create the `events` table in your MySQL database. Run the following SQL query to create the table:

```sql
CREATE TABLE events (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(255) NOT NULL,
 location VARCHAR(255) NOT NULL,
 date DATE NOT NULL,
 participants INT NOT NULL
);
```
API Documentation
Endpoints
GET /events: Retrieve all events.

GET /events/{event_id}: Retrieve details of a specific event.

POST /events: Schedule a new event.

Request Body Format:
json
```
{
    "name": "Event Name",
    "location": "Event Location",
    "date": "YYYY-MM-DD",
    "participants": 100
}
```
Response Format:
json
```
{
    "message": "Event scheduled successfully"
}
```
PUT /events/{event_id}: Update details of a specific event.

Request Body Format: Same as POST /events
Response Format:
```
{
    "message": "Event {event_id} updated successfully"
}
```
DELETE /events/{event_id}: Delete a specific event.

Response Format:
```
{
    "message": "Event {event_id} deleted successfully"
}
```
POST /schedule: Alias for POST /events. Schedule a new event.

Request Body Format: Same as POST /events
Response Format: Same as POST /events

### Authentication
The API uses basic authentication. Use the following credentials to authenticate:

Username: user
Password: password
Send the username and password as a Basic Authentication header with each request.

Example Usage
Schedule a New Event
Send a POST request to the /schedule endpoint with JSON data representing the event:
```
POST /schedule

Request Body:
{
    "name": "Birthday Party",
    "location": "Park",
    "date": "2024-03-25",
    "participants": 50
}
```
Retrieve All Events
Send a GET request to the /events endpoint:

```
GET /events
```

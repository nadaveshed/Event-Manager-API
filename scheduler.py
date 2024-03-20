from datetime import timedelta

from apscheduler.schedulers.background import BackgroundScheduler

# Initialize scheduler
scheduler = BackgroundScheduler()


# Function to send reminders
def send_reminder():
    # Implement logic to send reminder (e.g., send email or push notification)
    pass


# Schedule reminder tasks
def schedule_reminders(event_id, event_time):
    reminder_time = event_time - timedelta(minutes=30)
    scheduler.add_job(send_reminder, 'date', run_date=reminder_time, args=[event_id])


# Start the scheduler
scheduler.start()

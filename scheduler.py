import schedule
from sender import whatsapp_message
import datetime

def schedule_weekly(contacts, message, time_str, days):
    """
    Schedules a message to be sent at a given time on specified days of the week.
    Args:
        contacts (list): List of contact names.
        message (str): The message to send.
        time_str (str): Time in "HH:MM" format.
        days (list): List of days (e.g., ["Monday", "Wednesday", "Friday"]).
    """
    for day in days:
        if day.lower() == "monday":
            schedule.every().monday.at(time_str).do(whatsapp_message, contacts, message)
        elif day.lower() == "wednesday":
            schedule.every().wednesday.at(time_str).do(whatsapp_message, contacts, message)
        elif day.lower() == "friday":
            schedule.every().friday.at(time_str).do(whatsapp_message, contacts, message)
    print(f"Weekly messages scheduled for {days} at {time_str}")


def schedule_yearly(contacts, message, date_str, time_str):
    """
    Schedules a message to be sent once a year at a specific time.
    Args:
        contacts (list): List of contact names.
        message (str): The message to send.
        date_str (str): Date in "MM-DD" format.
        time_str (str): Time in "HH:MM" format.
    """
    def yearly_job():
        today = datetime.datetime.now().strftime("%m-%d")
        if today == date_str:
            whatsapp_message(contacts, message)

    schedule.every().day.at(time_str).do(yearly_job)
    print(f"Yearly message scheduled for {date_str} at {time_str}")

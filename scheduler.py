import schedule
from sender import whatsapp_message

def schedule_message(contacts, message, time_str):
    """
    Schedules a WhatsApp message to be sent at a specific time.
    Args:
        contacts (list): List of contact names.
        message (str): The message to send.
        time_str (str): Time in "HH:MM" format.
    """
    schedule.every().day.at(time_str).do(whatsapp_message, contacts, message)
    print(f"Message scheduled for {contacts} at {time_str}")

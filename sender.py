import pyautogui
import time
import datetime

def whatsapp_message(contacts, message):
    """
    Sends a WhatsApp message to multiple contacts.
    Args:
        contacts (list): List of contact names.
        message (str): The message to send.
    """
    try:
        print(f"Automation started at {datetime.datetime.now()}")

        # Open WhatsApp
        pyautogui.press("win")
        time.sleep(2)
        pyautogui.typewrite("WhatsApp")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(30)  

        for contact in contacts:
            # Search for the contact
            pyautogui.click(x=199, y=182) 
            time.sleep(5)
            pyautogui.typewrite(contact)
            time.sleep(2)
            pyautogui.click(x=217, y=279)  
            time.sleep(2)

            # Send the message
            pyautogui.typewrite(message)
            pyautogui.press("enter")
            time.sleep(30)  
            print(f"Message sent successfully to {contact}")

    except Exception as e:
        print(f"An error occurred: {e}")

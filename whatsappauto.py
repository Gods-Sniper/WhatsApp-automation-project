import pyautogui
import time
import schedule
import datetime

def whatsapp_message():
    try:
        print(f"Automation started at {datetime.datetime.now()}")
        
        
        pyautogui.press("win");time.sleep(2); pyautogui.typewrite("WhatsApp"); time.sleep(2);pyautogui.press("enter");time.sleep(2) 

        pyautogui.click(x=199, y=182);time.sleep(2)

        contact_name = "DFM"  
        pyautogui.typewrite(contact_name);time.sleep(2);pyautogui.press("enter");time.sleep(2)

        pyautogui.typewrite("Good Morning guys");pyautogui.press("enter")
        print(f"Message sent successfully to {contact_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

schedule.every().day.at("12:13").do(whatsapp_message)

print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(2)




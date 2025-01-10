from scheduler import schedule_message
import time
import schedule

if __name__ == "__main__":
   
    contacts = ["DFM", "Moi"]  
    message = "tsuips vas la bas c'est le automatic message qui donne, je viens d'arranger le pb"
    time_to_send = "08:58"  

    # Schedule the message
    schedule_message(contacts, message, time_to_send)

    # Keep the scheduler running
    print("Scheduler is running...")
    while True:
        schedule.run_pending()
        time.sleep(2)

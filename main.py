from scheduler import schedule_weekly, schedule_yearly
import schedule
import time

if __name__ == "__main__":
    
    weekly_contacts = ["DFM", "Sniper"] 
    weekly_message = "I did It!"
    weekly_time = "13:50"  
    weekly_days = ["Monday", "Wednesday", "Friday"]  


    schedule_weekly(weekly_contacts, weekly_message, weekly_time, weekly_days)

    birthday_contacts = ["DFM"]  
    birthday_message = "Happy Birthday! Wishing you a wonderful day!"
    birthday_date = "01-10"  
    birthday_time = "13:50" 

   
    schedule_yearly(birthday_contacts, birthday_message, birthday_date, birthday_time)

    
    print("Scheduler is running...")
    while True:
        schedule.run_pending()
        time.sleep(2)

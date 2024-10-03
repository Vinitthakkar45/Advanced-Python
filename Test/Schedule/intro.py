# import schedule
# import time

# def task():
#     print("I'm working...")

# schedule.every(5).seconds.do(task)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


import schedule
import time
import shutil
import os

def backup(source_folder, destination_folder):
    """
    Function to back up files from the source folder to the 
    destination folder.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for filename in os.listdir(source_folder):
            source_file= os.path.join(source_folder, filename)
            destination_file= os.path.join(destination_folder, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"Backedup: {filename}")
    except Exception as e:
        print(f"Errorduring backup: {e}")
# Define the source and destination folders
source_folder= "./yele"
destination_folder= "yelele"
# Schedule the backup task to run every day at 6:30 PM
schedule.every().day.at("22:44").do(backup, source_folder, 
destination_folder)
# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)

import schedule
import time

def Task1():
    print("Task 1 is created")
def Task2():
    print("Task 2 is created")
def Task3():
    print("Task 3 is created")

schedule.every(2).seconds.do(Task1)
schedule.every(5).seconds.do(Task2)
schedule.every().day.at("08:00").do(Task3)

while True:
    schedule.run_pending()
    time.sleep(1)
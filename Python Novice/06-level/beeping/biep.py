import time
import schedule

def doBiep():
    print("Biep!")

schedule.every().minute.at(":00").do(doBiep)

while True:
    schedule.run_pending()
    time.sleep(1)

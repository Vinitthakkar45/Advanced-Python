from time import sleep
import threading

class CustomThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(15):
            print(f"Hello {self.name} ", i)
            sleep(1)

t1 = CustomThread(name="Paddi")
t2 = CustomThread(name="Saad")

t1.start()
t2.start()

t1.join()
t2.join()
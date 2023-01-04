import requests
import json
import threading
import time


ip="http://127.0.0.1:5000"



def send(status):
    response=requests.post(ip,{"status":status})
    print(response.json())



t1 = threading.Thread(target=send, args=("nummer 1",))
t2 = threading.Thread(target=send, args=("nummer 2",))
t3 = threading.Thread(target=send, args=("STOP",))
 
# starting thread 1
t1.start()
# starting thread 2
t2.start()
for i in range(5):
    time.sleep(1)
    print(i,"/", 4)
print("Jetzt gehts los!")
t3.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
t3.join()

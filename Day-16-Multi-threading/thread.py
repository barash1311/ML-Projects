### multithreading
##when to use multi threading
## i/o operation tasks that spend i/o
import threading
import time 
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"numbers:{i}")
def print_letters():
    for i in "abcde":
        time.sleep(1)
        print(f"letters:{i}")
        
        
##create two thread
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()
print(t)
##start thr thread
t1.start()
t2.start()
t1.join()
t2.join()
finised_time=time.time()-t
print(finised_time)
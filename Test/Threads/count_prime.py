import threading

sum = 0
sum_lock = threading.Lock()

def thread_function(val1, val2):
    global sum
    for i in range(val1, val2):
        is_prime = True
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime :
            print(f"{i} is prime")
            with sum_lock:
                sum += i
        
t1 = threading.Thread(target=thread_function, args=(2, 2500))
t2 = threading.Thread(target=thread_function, args=(2500, 5000))
t3 = threading.Thread(target=thread_function, args=(5000, 7500))
t4 = threading.Thread(target=thread_function, args=(7500, 10000))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(sum)
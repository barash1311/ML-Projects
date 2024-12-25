import multiprocessing
import math
import sys
import time
sys.set_int_max_str_digits(100000)

#factorial function
def compute_fact(numbers):
    print(f"factorial of numbers:{numbers}")
    result=math.factorial(numbers)
    print(f"the facotiral of {numbers} is {result}")
    return result

if __name__=="__main__":
    numbers=[500,455,8000]
    start=time.time()
    print(start)
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_fact,numbers)
    end_time=time.time()-start
    print(end_time)
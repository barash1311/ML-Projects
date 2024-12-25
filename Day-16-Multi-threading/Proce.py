from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(10)
    return f"square:{number*number}"
numbers=[0,1,2,3,4,5,6,7]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_numbers,numbers)
        

    for result in results:
            print(result)
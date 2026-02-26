#wapp to find how much time is being taken to run your programme 
import time

def my_program():
    total = 0
    for i in range(1000000):
        total += i
    return total


start_time = time.time()

my_program()


end_time = time.time()


print("Time taken:", end_time - start_time, "seconds")

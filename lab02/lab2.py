import time
from numpy import random
initial = random.randint(1000000, size=(1000000))
#insertion sort
def insort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array


#bubble sort
def busort(my_array):
    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

start_time = time.time()
insort(initial)
first = time.time() - start_time
print("Insertion sort takes %s seconds" % round(first, 3))
busort(initial)
second = (time.time() - start_time - first)
print("Bubble sort takes %s seconds" % round(second, 3))

from math import sqrt

def JumpSearch(arr, key):
    n = len(arr)
    low = 0
    jump = int(sqrt(n))    #  jump size
    high = min(jump, n)  
   
    while low < n and arr[high - 1] < key:
        low = high
        high = min(low + jump, n)

    if low < n and arr[high - 1] >= key:
        return Linear(arr[low:high], key, low)    # linear search in the range

    return -1 

def Linear(arr, key, offset):
    for i in range(len(arr)):
        if arr[i] == key:
            return offset + i  
    return -1  


arr = [2, 4, 7, 10, 15, 20, 25, 30, 35, 40,50,60]
key = 35
result = JumpSearch(arr, key)
print(result)
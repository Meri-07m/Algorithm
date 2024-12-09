def Linear(arr, key):
    ind = -1
    for i in range(len(arr)):
        if arr[i] == key:
            ind = i
    return ind

arr = [15, 3, 8, 25, 42, 9, 4]
key = 42
result = Linear(arr,key)
print(result)
def ExponentialSearch(arr, key):
    if arr[0] == key:
        return 0
    
    n = len(arr)
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2  

    # binary search in the range (i//2 to min(i, n-1))
    return BinarySearch(arr, key, i // 2, min(i, n - 1))

def BinarySearch(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
key = 90
result = ExponentialSearch(arr, key)
print(result)
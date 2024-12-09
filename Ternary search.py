def Ternary(arr, key):
    L = 0  # Left index
    R = len(arr) - 1  # Right index

    while L <= R:
        mid1 = L + (R - L) // 3
        mid2 = R - (R - L) // 3

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2

        # search in the left part
        elif key < arr[mid1]:
            R = mid1 - 1

        # search in the right part
        elif key > arr[mid2]:
            L = mid2 + 1

        # key is between mid1 and mid2,  search the middle part
        else:
            L = mid1 + 1
            R = mid2 - 1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 23
result = Ternary(arr, key)
print(result)
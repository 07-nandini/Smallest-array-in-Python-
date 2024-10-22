def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]

print("Smallest in arr1:", find_smallest(arr1))  
print("Smallest in arr2:", find_smallest(arr2))  

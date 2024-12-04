import random
def bubble_sort(arr):
    n = len(arr)
    
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

def is_sorted(arr):
    
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)  
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bogosort(arr)
print("Sorted array:", sorted_arr)
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

def is_sorted(arra):
    
    return all(arra[i] <= arra[i+1] for i in range(len(arr)-1))

def bogosort(arra):
    while not is_sorted(arra):
        random.shuffle(arra)  
    return arra


arra = [65, 35, 20, 10, 28, 19, 9]
sorted_arra = bogosort(arra)
print(sorted_arra)
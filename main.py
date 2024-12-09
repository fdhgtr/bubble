import random
array = [34, 7, 23, 32, 5, 62, 32, 9, 54, 18]
print("Původní pole:", array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
    return array


sorted_array = bubble_sort(array)
print("Bubble sort:", sorted_array)


def bogo_sort(array):
    
    def is_sorted(array):
        return array == sorted(array)
    
    
    while not is_sorted(array):
        random.shuffle(array)  
    return array
sorted_array2 = bogo_sort(array.copy())
print("Bogo Sort:", sorted_array2)


def selection_sort(array):
    for m in range(len(array)):
        
        nejmenší = m
        for k in range(m + 1, len(array)):
            if array[k] < array[nejmenší]:
                nejmenší = k
        
        array[m], array[nejmenší] = array[nejmenší], array[m]
    return array


sorted_array3 = selection_sort(array.copy())
print("Selection Sort:", sorted_array3)

def insertion_sort(array):
    for q in range(1, len(array)):
        lol = array[q]
        n = q - 1
        
        
        while n >= 0 and array[n] > lol:
            array[n + 1] = array[n]
            n -= 1
        
        
        array[n + 1] = lol
    
    return array

sorted_array4 = insertion_sort(array.copy())
print("Insertion Sort:", sorted_array4)
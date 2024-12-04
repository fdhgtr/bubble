import random
array = [34, 7, 23, 32, 5, 62, 32, 9, 54, 18]
print("Původní pole:", array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
    return array


sorted_arr = bubble_sort(array)
print("Seřazené pole:", sorted_arr)

def bogosort(arrayb):
    count = 0
    while not is_sorted(arrayb):
        random.shuffle(arrayb)
        count += 1
        print(f"Pokus {count}: {arrayb}")
    print(f"Sorted array after {count} shuffles: ")
    bogosort(arrayb)
    print("Bogo",arrayb)


def selection_sort(array):
    for m in range(len(array)):
        
        nejmenší = m
        for k in range(m + 1, len(array)):
            if array[k] < array[nejmenší]:
                nejmenší = k
        
        array[m], array[nejmenší] = array[nejmenší], array[m]
    return array


sorted_arr_selection = selection_sort(array.copy())
print("Seřazené pole Selection Sort:", sorted_arr_selection)
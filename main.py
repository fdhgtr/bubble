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


def selection_sort(arr):
    for i in range(len(arr)):
        
        nejmenší = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[nejmenší]:
                nejmenší1 = j
        
        arr[i], arr[nejmenší1] = arr[nejmenší1], arr[i]
    return arr


sorted_arr_selection = selection_sort(arr.copy())
print("Seřazené pole (Selection Sort):", sorted_arr_selection)
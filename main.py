arr = [34, 7, 23, 32, 5, 62, 32, 9, 54, 18]
print("Původní pole:", arr)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr


sorted_arr = bubble_sort(arr)
print("Seřazené pole:", sorted_arr)


def selection_sort(arr):
    for i in range(len(arr)):
        
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


sorted_arr_selection = selection_sort(arr.copy())
print("Seřazené pole (Selection Sort):", sorted_arr_selection)

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
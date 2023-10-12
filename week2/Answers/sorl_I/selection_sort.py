# time complexity of this sorting is O of n square
def selectionSort(arr):
    for i in range(0, len(arr)):

        min_index = i

        for j in range(i, len(arr)):

            if arr[min_index] >= arr[j]:
                min_index = j

        if arr[i] >= arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



arr = [1, 4, 2, 7, 3, 9, 2]
sorted_arr = selectionSort(arr)
print("Sorted Array is : ",sorted_arr)
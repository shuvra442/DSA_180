def pivot(arr, low, high):
    i = low
    pivotElement = arr[low]

    for j in range(low + 1, high + 1):
        if arr[j] < pivotElement:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    return i

def quickSort(arr, low, high):
    if low < high:
        partitionIndex = pivot(arr, low, high)
        quickSort(arr, low, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, high)

arr = [1, 4, 2, 7, 3, 9, 2]
quickSort(arr, 0, len(arr) - 1)
print("Sorted Array is:", arr)

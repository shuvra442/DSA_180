def insertionSort(arr):
    n = len(arr)

    # Iterate through the array, starting from the second element (index 1).
    for i in range(1, n):
        # Store the current element in a variable.
        current_element = arr[i]
        j = i

        # Compare the current element with the elements in the sorted subarray
        # and shift elements to the right until we find the correct position.
        while j > 0 and current_element < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        # Place the current element in its correct sorted position.
        arr[j] = current_element

    return arr

arr = [1, 4, 2, 7, 3, 9, 2]
sorted_arr = insertionSort(arr)
print("Sorted Array is:", sorted_arr)

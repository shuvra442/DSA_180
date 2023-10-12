def recursive_insertion_sort(arr, n):
    # Base case: If the array has only one element or is empty, it is already sorted.
    if n <= 1:
        return

    # Recursively sort the first (n-1) elements.
    recursive_insertion_sort(arr, n - 1)

    # Insert the last element (the nth element) into its correct position in the sorted array.
    last_element = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last_element:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last_element

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

recursive_insertion_sort(arr, n)

print("Sorted array is:", arr)

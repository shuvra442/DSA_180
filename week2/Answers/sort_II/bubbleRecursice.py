# recursive bubble sort

def bubble_sort_recursive(arr, n):
    # Base case: If the array has only one element or is empty, it is already sorted.
    if n == 1:
        return

    # Perform a single pass of bubble sort on the array.
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements if they are in the wrong order.

    # Recursively sort the remaining (n-1) elements.
    bubble_sort_recursive(arr, n - 1)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

bubble_sort_recursive(arr, n)

print("Sorted array is:", arr)

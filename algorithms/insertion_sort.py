def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Insertion Sort builds the sorted list one element at a time by comparing each
    new element with those before it and inserting it into the correct position.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in-place.
    """
    for i in range(1, len(arr)):
        key = arr[i]              # current element to insert
        j = i - 1

        # shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1

        arr[j + 1] = key          # insert key at the correct position

    return arr 
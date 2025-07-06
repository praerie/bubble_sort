def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm (in-place).

    This algorithm repeatedly selects the smallest remaining element
    and places it at the beginning of the unsorted portion of the list.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list (same object as input).
    """
    n = len(arr)

    for i in range(n):
        min_index = i  # assume current index is the minimum

        # find the index of the smallest element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap if a smaller element was found
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

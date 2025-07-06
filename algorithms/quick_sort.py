def quick_sort(arr):
    """
    Sorts a list in ascending order using the Quick Sort algorithm (in-place).

    This version improves performance on sorted or duplicate-heavy inputs
    by selecting the middle element as the pivot instead of the last,
    reducing the chance of unbalanced partitions and deep recursion.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The list is sorted in-place.
    """

    def partition(low, high):
        # choose the middle element as pivot to reduce chance of worst-case performance
        mid = (low + high) // 2
        pivot = arr[mid]

        # move pivot to the end of the current segment for convenience
        arr[mid], arr[high] = arr[high], arr[mid]

        i = low  # tracks position to place the next smaller-than-pivot value

        # rearrange elements: all smaller than pivot go to the left
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # place pivot in its correct position
        arr[i], arr[high] = arr[high], arr[i]
        return i 

    def _quick_sort(low, high):
        if low < high:
            pivot_index = partition(low, high)  # partition the array around the pivot
            _quick_sort(low, pivot_index - 1)   # recursively sort the left side
            _quick_sort(pivot_index + 1, high)  # recursively sort the right side

    _quick_sort(0, len(arr) - 1)  # initial call to the recursive sort

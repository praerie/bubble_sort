def quick_sort(arr):
    """
    Recursively sorts a list using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that selects a pivot element
    and partitions the array into two halves: elements less than the pivot and
    elements greater than the pivot. It then recursively sorts both halves.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements in ascending order.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]                                  # choose the first element as the pivot
    less = [x for x in arr[1:] if x <= pivot]       # elements less than or equal to pivot
    greater = [x for x in arr[1:] if x > pivot]     # elements greater than pivot

    return quick_sort(less) + [pivot] + quick_sort(greater)

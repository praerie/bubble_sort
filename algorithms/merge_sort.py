def merge_sort(arr):
    """
    Recursively sorts a list using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that splits the list into halves,
    recursively sorts each half, and then merges the sorted halves into a final sorted list.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements in ascending order.
    """
    # base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list (helper function).

    Parameters:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
    result = []
    i = j = 0

    # compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append any remaining elements from either half
    result.extend(left[i:])
    result.extend(right[j:])
    return result

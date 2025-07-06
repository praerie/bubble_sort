def heap_sort(arr):
    """
    Sorts a list in ascending order using the Heap Sort algorithm.

    Heap Sort builds a max heap from the input list,
    then repeatedly extracts the largest element (the root) and places it
    at the end of the list. The heap is then rebuilt for the remaining elements.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The input list is sorted in-place.
    """
    n = len(arr)

    # build a max heap from the input list
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move current root to end
        heapify(arr, i, 0)               # "heapify" the reduced heap


def heapify(arr, heap_size, root_index):
    """
    Maintains the max-heap property for a subtree rooted at index root_index (helper function).

    Parameters:
        arr (list): The list representing the heap.
        heap_size (int): The size of the heap (may be smaller than len(arr)).
        root_index (int): The index of the root of the subtree to heapify.

    Returns:
        None: The list is modified in-place.
    """
    largest = root_index               # assume root is the largest
    left = 2 * root_index + 1          # left child index
    right = 2 * root_index + 2         # right child index

    # check if left child exists and is greater than the root
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # check if right child exists and is greater than the largest so far
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # if the largest is not the root, swap and continue heapifying
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)

def bubble_sort(input_list):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.
    If no swaps occur during a full pass, the algorithm exits early, as the list is already sorted.

    Parameters:
        input_list (list): A list of comparable elements (e.g., integers or floats).

    Returns:
        list: The same list sorted in ascending order.
    """
    n = len(input_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if out of order
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
    return input_list
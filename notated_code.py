def bubbleSort(arr):  # O(1): definition only, no runtime impact
    n = len(arr)  # O(1): getting list length is constant time
    swapped = False  # O(1): assigning a boolean variable is constant time

    for i in range(n - 1):  # O(n): outer loop runs n - 1 times
        for j in range(0, n - i - 1):  # O(n - i - 1) per i: inner loop decreases with each pass
            if arr[j] > arr[j + 1]:  # O(1): comparing two elements is constant time
                swapped = True  # O(1): setting a boolean flag is constant time
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1): swapping two elements is constant time
        if not swapped:  # O(1): checking a boolean condition is constant time
            return  # O(1): returning exits the function in constant time

# time constant: does not depend on input size (n), described in Big-O notation as O(1)
# linear time: runtime grows in direct proportion to input size (n), described in Big-O notation as O(n)

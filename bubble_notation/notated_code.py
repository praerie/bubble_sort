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

"""
Build equation based on N and (c):

The outer loop of the code runs from i = 0 to n - 2, which is (n - 1) iterations -> O(n).
For each iteration of i, the inner loop runs (n - i - 1) times.

Total number of comparisons: (n - 1) + (n - 2) + (n - 3) + ... + 1
This is a known arithmetic series (a triangular number), which sums to n(n - 1)/2.

Each comparison and potential swap inside the loop is constant time -> O(1).

Total time: T(n) = O(n(n - 1)/2) × O(1)
Simplified equation: T(n) = O(n²)

T(n) = O(n(n - 1)/2) × O(1) comes from counting how many comparisons happen 
in the worst-case scenario of bubble sort. In the worst-case scenario, 
we assume that every possible comparison and swap is executed, 
e.g. when the input list is in completely reverse order.

The n(n - 1)/2 part represents the total number of comparisons;
the inner loop runs fewer times with each outer iteration.

In Big-O notation, we ignore constants and lower-order terms
because they don't change the overall growth pattern, so we drop the /2 and the -1. 
The simplified equation is therefore T(n) = O(n²), which reflects how the time 
increases most significantly as the input size gets larger.
"""




def bubbleSort(arr): 
    n = len(arr) 
    swapped = False 

    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j + 1]: 
                swapped = True 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
        if not swapped: 
            return

if __name__ == "__main__":
    test_arr = [64, 36, 25, 12, 23, 11, 90]
    print("Original array:", test_arr)
    bubbleSort(test_arr)
    print("Sorted array:", test_arr)



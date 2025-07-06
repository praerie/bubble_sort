from algorithms.merge_sort import merge_sort

def test_merge_sort():
    # test case 1: random order
    assert merge_sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]

    # test case 2: already sorted
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # test case 3: reverse order
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # test case 4: all elements the same
    assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    # test case 5: empty list
    assert merge_sort([]) == []

    # test case 6: single element
    assert merge_sort([42]) == [42]

    print("All merge_sort tests passed!")

if __name__ == "__main__":
    test_merge_sort()

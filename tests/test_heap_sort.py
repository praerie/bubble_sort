from algorithms.heap_sort import heap_sort

def test_heap_sort():
    # test case 1: random order
    data = [3, 1, 4, 1, 5, 9]
    heap_sort(data)
    assert data == [1, 1, 3, 4, 5, 9]

    # test case 2: already sorted
    data = [1, 2, 3, 4, 5]
    heap_sort(data)
    assert data == [1, 2, 3, 4, 5]

    # test case 3: reverse order
    data = [5, 4, 3, 2, 1]
    heap_sort(data)
    assert data == [1, 2, 3, 4, 5]

    # test case 4: all elements the same
    data = [7, 7, 7, 7]
    heap_sort(data)
    assert data == [7, 7, 7, 7]

    # test case 5: empty list
    data = []
    heap_sort(data)
    assert data == []

    # test case 6: single element
    data = [42]
    heap_sort(data)
    assert data == [42]

    print("All heap_sort tests passed!")

if __name__ == "__main__":
    test_heap_sort()

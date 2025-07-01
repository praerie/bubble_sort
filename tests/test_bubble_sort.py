from algorithms.bubble_sort import bubble_sort

def test_bubble_sort():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([5, 3, 8, 1], [1, 3, 5, 8]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([2, 3, 2, 1, 1], [1, 1, 2, 2, 3]),
        ([4, 4, 4, 4], [4, 4, 4, 4]),
        ([10, -1, 3, 0, 2], [-1, 0, 2, 3, 10]),
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        result = bubble_sort(input_list.copy())
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
        print(f"Test {i} passed.")

if __name__ == "__main__":
    test_bubble_sort()

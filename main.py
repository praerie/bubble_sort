from utils.dataset_utils import load_dataset
from utils.benchmark_utils import time_sorting
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.heap_sort import heap_sort
from algorithms.quick_sort import quick_sort
from algorithms.insertion_sort import insertion_sort
import os

def main():
    filenames = sorted(os.listdir("datasets"))

    # # bubble sort 
    # for file in filenames:
    #     data = load_dataset(file)
    #     duration = time_sorting(bubble_sort, data.copy())
    #     print(f"{file:<25} | Time: {duration:.2f} ms")

    # # merge sort
    # for file in filenames:
    #     data = load_dataset(file)
    #     duration = time_sorting(merge_sort, data.copy())
    #     print(f"{file:<25} | Time: {duration:.2f} ms")

    # # heap sort
    # for file in filenames:
    #     data = load_dataset(file)
    #     duration = time_sorting(heap_sort, data.copy())
    #     print(f"{file:<25} | Time: {duration:.2f} ms")

    # # quick sort
    # for file in filenames:
    #     data = load_dataset(file)
    #     duration = time_sorting(quick_sort, data.copy())
    #     print(f"{file:<25} | Time: {duration:.2f} ms")

    # insertion sort 
    for file in filenames:
        data = load_dataset(file)
        duration = time_sorting(insertion_sort, data.copy())
        print(f"{file:<25} | Time: {duration:.2f} ms")

if __name__ == "__main__":
    main()
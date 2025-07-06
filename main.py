from utils.dataset_utils import load_dataset
from utils.benchmark_utils import time_sorting
from algorithms.bubble_sort import bubble_sort
import os

def main():
    filenames = sorted(os.listdir("datasets"))
    for file in filenames:
        data = load_dataset(file)
        duration = time_sorting(bubble_sort, data.copy())
        print(f"{file:<25} | Time: {duration:.2f} ms")

if __name__ == "__main__":
    main()
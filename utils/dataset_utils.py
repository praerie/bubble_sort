import os
import random

# sizes of datasets
DATASET_SIZES = {
    "small": 100,
    "medium": 1_000,
    "large": 10_000,
    "very_large": 100_000
}

# output folder
OUTPUT_DIR = "datasets"

# generate list of ints based on given size and kind
def generate_data(size, kind):
    if kind == "random":
        # list of unique random ints
        return random.sample(range(size * 10), size)  
    elif kind == "sorted":
        # sorted list from 0 to size -1
        return list(range(size))  
    elif kind == "reverse":
        # reverse-sorted list from 'size' down to 1
        return list(range(size, 0, -1))  
    elif kind == "duplicates":
        # list with repeated ints, choosing randomly from small range
        return [random.choice(range(size // 10)) for _ in range(size)]  
    else:
        raise ValueError("Unknown data kind")

# save list of ints to .txt file, separated by spaces
def save_dataset(data, name):
    path = os.path.join(OUTPUT_DIR, name + ".txt")
    with open(path, "w") as f:
        # convert ints to strings and join with spaces
        f.write(" ".join(map(str, data)))  

# load list of ints from .txt file
def load_dataset(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "r") as f:
        return list(map(int, f.read().split()))

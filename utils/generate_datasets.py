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

def generate_data(size, kind):
    if kind == "random":
        return random.sample(range(size * 10), size)
    elif kind == "sorted":
        return list(range(size))
    elif kind == "reverse":
        return list(range(size, 0, -1))
    elif kind == "duplicates":
        return [random.choice(range(size // 10)) for _ in range(size)]
    else:
        raise ValueError("Unknown data kind")
    
def save_dataset(data, name):
    path = os.path.join(OUTPUT_DIR, name + ".txt")
    with open(path, "w") as f:
        f.write(" ".join(map(str, data)))

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    kinds = ["random", "sorted", "reverse", "duplicates"]

    for kind in kinds:
        for label, size in DATASET_SIZES.items():
            data = generate_data(size, kind) 
            filename = f"{label}_{kind}"
            save_dataset(data, filename)
            print(f"Saved: {filename}.txt")

if __name__ == "__main__":
    main()
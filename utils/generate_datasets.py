from utils.dataset_utils import generate_data, save_dataset, DATASET_SIZES, OUTPUT_DIR
import os

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # create output folder if it doesn't exist
    kinds = ["random", "sorted", "reverse", "duplicates"]  # input scenarios

    for kind in kinds:
        for label, size in DATASET_SIZES.items():
            data = generate_data(size, kind)    # generate dataset
            filename = f"{label}_{kind}"        # filename example: "small_random"
            save_dataset(data, filename)        # save to file
            print(f"Saved: {filename}.txt")     # saved confirmation print

if __name__ == "__main__":
    main()
from datasets import load_from_disk,concatenate_datasets
if __name__ == "__main__":
    # Specify the local directory where you want to save the dataset
    path = [
        "./updated_sticky_notes_100_max"
    ]
    dataset_list=[]
    # ./mixer_dataset_combined
    for local_path in path:
        # Load the dataset from the local directory
        loaded_dataset = load_from_disk(local_path)

        # Now you can work with the loaded_dataset
        print(loaded_dataset[99]["stickyNotes"])
        print(len(loaded_dataset))
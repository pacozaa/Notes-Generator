from datasets import load_from_disk,concatenate_datasets
if __name__ == "__main__":
    # Specify the local directory where you want to save the dataset
    path = [
        "./dataset/mixer_dataset_combined_2000",
        "./dataset/mixer_dataset_combined",
        "./dataset/mixer_dataset_combined_5000",
        "./dataset/mixer_dataset_combined_10k",
        "./dataset/mixer_dataset_combined_20k",
    ]
    dataset_list=[]
    # ./mixer_dataset_combined
    for local_path in path:
        # Load the dataset from the local directory
        loaded_dataset = load_from_disk(local_path)

        # Now you can work with the loaded_dataset
        print(loaded_dataset)
        # print(loaded_dataset.column_names)
        # print(len(loaded_dataset))
        # print(loaded_dataset[50])
        # print(len(loaded_dataset[50]["notes"]))
        dataset_list.append(loaded_dataset)

    combined_dataset = concatenate_datasets(dataset_list)
    print(len(combined_dataset))
    combined_dataset.push_to_hub("pacozaa/sticky_notes")
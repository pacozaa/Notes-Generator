from datasets import load_from_disk
def main():
    # list
    # Specify the local directory where you want to save the dataset
    path = [
        "./dataset/conversations/TeamPersonaHub_Conversations_6cb4d8b2-052d-48e8-a08d-65e0f2fd17c9"
    ]
    dataset_list=[]
    # ./mixer_dataset_combined
    for local_path in path:
        # Load the dataset from the local directory
        loaded_dataset = load_from_disk(local_path)

        # Now you can work with the loaded_dataset
        print(loaded_dataset[0])
        print(len(loaded_dataset))
        # print(loaded_dataset)

if __name__ == "__main__":
    main()
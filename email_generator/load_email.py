import random
from datasets import load_from_disk
def main():
    # list
    # Specify the local directory where you want to save the dataset
    path = [
        "./dataset/emails/PersonaHub_emails_50_gpt-4o-mini_d732284d-9892-4a6a-9c1c-e57b9ac526fe"
    ]
    
    # ./mixer_dataset_combined
    for local_path in path:
        # Load the dataset from the local directory
        loaded_dataset = load_from_disk(local_path)

        # Now you can work with the loaded_dataset
        print(random.choice(loaded_dataset))
        print(len(loaded_dataset))
        # print(loaded_dataset)

if __name__ == "__main__":
    main()
from datasets import load_from_disk,concatenate_datasets
def main():

    path = [
       "./dataset/emails/PersonaHub_emails_50_gpt-4o-mini_d732284d-9892-4a6a-9c1c-e57b9ac526fe",
       "./dataset/emails/PersonaHub_emails_50_gpt-4o-mini_2becf9a7-988c-4e01-8ca4-e18f39fed2df",
       "./dataset/emails/PersonaHub_emails_150_gpt-4o-mini_40cb06ca-caad-46c2-8c30-faf718a7f5a6",

    ]
    dataset_list=[]
    # ./mixer_dataset_combined
    for local_path in path:
        # Load the dataset from the local directory
        loaded_dataset = load_from_disk(local_path)

        # Now you can work with the loaded_dataset
        # print(loaded_dataset)
        # print(loaded_dataset.column_names)
        # print(len(loaded_dataset))
        # print(loaded_dataset[50])
        # print(len(loaded_dataset[50]["notes"]))
        dataset_list.append(loaded_dataset)

    combined_dataset = concatenate_datasets(dataset_list).shuffle()
    print(len(combined_dataset))
    # print(combined_dataset)
    combined_dataset.push_to_hub("pacozaa/PersonaHub_Email")

if __name__ == "__main__":
    main()
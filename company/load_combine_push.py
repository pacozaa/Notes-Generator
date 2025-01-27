from datasets import load_from_disk,concatenate_datasets
if __name__ == "__main__":
    # File List
# TeamPersonaHub_business_500_4o_54f33b57-1040-4921-a95a-ceb6b19f6102
# TeamPersonaHub_business_500_4o_93128519-93a5-4409-b977-dd9cf5fd556a
# TeamPersonaHub_business_500_4o_bb7cd351-d238-4055-92b7-5260558cb687
# TeamPersonaHub_business_500_4o_dde8cd0c-cd64-4931-82d6-c0930d25be38
    path = [
        "./dataset/sticky_notes/TeamPersonaHub_business_500_4o_54f33b57-1040-4921-a95a-ceb6b19f6102",
        "./dataset/sticky_notes/TeamPersonaHub_business_500_4o_93128519-93a5-4409-b977-dd9cf5fd556a",
        "./dataset/sticky_notes/TeamPersonaHub_business_500_4o_bb7cd351-d238-4055-92b7-5260558cb687",
        "./dataset/sticky_notes/TeamPersonaHub_business_500_4o_dde8cd0c-cd64-4931-82d6-c0930d25be38"
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
    print(combined_dataset)
    combined_dataset.push_to_hub("pacozaa/TeamPersonaHub_Business_StickyNotes_Batch_2")
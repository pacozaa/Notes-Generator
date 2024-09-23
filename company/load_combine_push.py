from datasets import load_from_disk,concatenate_datasets
if __name__ == "__main__":
    
    path = [
        "./dataset/sticky_notes/TeamPersonaHub_business_4o_4941577b-b1f5-4c87-83af-802f183b0e11",
        "./dataset/sticky_notes/TeamPersonaHub_business_4o_e2940101-a9f5-43b3-be58-82ff3505fadb",
        "./dataset/sticky_notes/TeamPersonaHub_business_4o_eea86a0a-4812-4346-9a3b-3f1b8ddebd69",
        "./dataset/sticky_notes/TeamPersonaHub_business_4o_f492f7df-6ab8-40b7-98bb-5a13efc9f837"
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

    combined_dataset = concatenate_datasets(dataset_list).shuffle(52)
    print(len(combined_dataset))
    # combined_dataset.push_to_hub("pacozaa/TeamPersonaHub_Business_StickyNotes")
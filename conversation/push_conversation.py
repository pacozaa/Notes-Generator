from datasets import load_from_disk,concatenate_datasets
def main():
#     TeamPersonaHub_Conversations_6cb4d8b2-052d-48e8-a08d-65e0f2fd17c9
# TeamPersonaHub_Conversations_b39ef831-c884-4958-b446-004ba19560b9
# TeamPersonaHub_Conversations_ccab736d-fe66-4a2e-9a16-7f189c2abea5
# TeamPersonaHub_Conversations_f42192cb-26d0-494d-8f4d-382525ccfec1
    path = [
        "./dataset/conversations/TeamPersonaHub_Conversations_6cb4d8b2-052d-48e8-a08d-65e0f2fd17c9",
        "./dataset/conversations/TeamPersonaHub_Conversations_b39ef831-c884-4958-b446-004ba19560b9",
        "./dataset/conversations/TeamPersonaHub_Conversations_ccab736d-fe66-4a2e-9a16-7f189c2abea5",
        "./dataset/conversations/TeamPersonaHub_Conversations_f42192cb-26d0-494d-8f4d-382525ccfec1"
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
    combined_dataset.push_to_hub("pacozaa/TeamPersonaHub_Conversation")

if __name__ == "__main__":
    main()
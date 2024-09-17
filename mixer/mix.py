from datasets import load_dataset, Dataset,concatenate_datasets
from functools import partial
import random
from tqdm import tqdm
import time
from dataset_list import dataset_list
from extract import extract_sentences
from utils import closest_divisible_number
from save_to_file import saveToFile
# from mixer.dataset_list import dataset_list
# from mixer.extract import extract_sentences
# from mixer.save_to_file import saveToFile
# main
def modify_column(example, needed_column):
    # Example: Convert the "text" column to uppercase
    example["text"] = example[needed_column]
    return example
# Define the mapping function with an additional argument
def modify_column(batch, needed_column):
    # Example: Convert the "text" column to uppercase
    batch["text"] = [text for text in batch[needed_column]]
    return batch

if __name__ == "__main__":
    # Create a list of ranges
    
    
    notes = []
    sample_size=50
    
    # sleep 5 seconds
    # time.sleep(5)
    dataset_len=[]
    dataset_list_data=[]
    print(f"""Total dataset_list Length: {len(dataset_list)}""")
    # print(dataset_list)
    for [index, dataset_data] in enumerate(dataset_list):
        # print(f"""Loading.....{dataset_data["name"]}""")
        dataset_name=dataset_data["name"]
        # Load Dataset
        dataset = load_dataset(dataset_name, split="train")
        dataset_list[index]["dataset"]=dataset
        print(f"""Dataset {dataset_name} loaded successfully.""")
        print(f"""Total Length: {len(dataset)}""")
        dataset_len.append(len(dataset))
        # Define the mapping function with an additional argument
        

        # Create a partial function with the additional argument pre-filled
        partial_modify_column = partial(modify_column, needed_column=dataset_data["column"])
        
        # Apply the partial function to the dataset
        modified_dataset = dataset.map(partial_modify_column, batched=True)
        # Remove all columns except 'text'
        modified_dataset = modified_dataset.remove_columns([col for col in dataset.column_names if col != 'text'])
        # print(modified_dataset)
        dataset_list_data.append(modified_dataset)

    combined_dataset = concatenate_datasets(dataset_list_data).shuffle(52)
    # # print minimum length
    # print(f"""Minimum dataset_len Length: {min(dataset_len)}""")
    # print(dataset_len)
    print(f"""Combined dataset Length: {len(combined_dataset)}""")
    # len(combined_dataset)
    valid_range = 100
    max_valid_range = closest_divisible_number(len(combined_dataset),valid_range)
    print(f"""Combined dataset Valid Length: {len(combined_dataset)}""")
    ranges_list = [range(i, i + valid_range) for i in range(0, max_valid_range, valid_range)]
    print(f"""Total Ranges: {len(ranges_list)}""")
    for selectRange in tqdm(ranges_list, desc="Processing Range"):
        all_sentences=[]
        all_words=[]
        all_mix=[]
        
        dataset = dataset_list[index]["dataset"]            
        column_name=dataset_data["column"]
        # Print all the column names in the dataset
        # print(dataset["train"].column_names)            
        sentences, words, mix = extract_sentences(combined_dataset.select(selectRange),sample_size,"combined","text")
        all_sentences = all_sentences + sentences
        all_words = all_words + words
        all_mix = all_mix + mix

        random.shuffle(all_sentences)
        random.shuffle(all_words)
        random.shuffle(all_mix)
            
        # print(f"""Total sentences: {len(all_sentences)}""")
        # print(f"""Total words: {len(all_words)}""")
        # print(f"""Total mix: {len(all_mix)}""")

        # Truncate the sentences list to the first 50 sentences
        all_sentences = all_sentences[:100]
        all_words = all_words[:150]
        all_mix = all_mix[:150]
        if False:
            saveToFile(f"all_sentences","",all_sentences)
            saveToFile(f"all_words","",all_words)
            saveToFile(f"all_mix","",all_mix)
        notes.append(all_sentences)
        # notes.append(all_words)
        # notes.append(all_mix)
        if False:
            # Create a dataset with the "notes" column
            dataset_combined = Dataset.from_dict({"stickyNotes": notes})

            # Save the dataset to local disk
            # dataset_combined.push_to_hub("pacozaa/sticky_notes")
            dataset_combined.save_to_disk(f"""./mixer_dataset_combined_{selectRange}""")

            print(f"""Combined dataset saved successfully at {selectRange}""")

    if True:
        # Create a dataset with the "notes" column
        dataset_combined = Dataset.from_dict({"stickyNotes": notes})

        # Save the dataset to local disk
        # dataset_combined.push_to_hub("pacozaa/sticky_notes")
        dataset_combined.save_to_disk(f"""./mixer_dataset_combined_100_each_all_{max_valid_range}""")
        print(f""" mixer_dataset_combined_all Total Length: {max_valid_range}""")

        print("Combined dataset saved successfully.")
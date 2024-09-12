from datasets import load_dataset, Dataset
import random
from tqdm import tqdm
import time
from dataset_list import dataset_list
from extract import extract_sentences
from save_to_file import saveToFile
# from mixer.dataset_list import dataset_list
# from mixer.extract import extract_sentences
# from mixer.save_to_file import saveToFile
# main
if __name__ == "__main__":
    # Create a list of ranges
    ranges_list = [range(i, i + 100) for i in range(0, 20000, 100)]
    
    notes = []
    sample_size=50
    print(len(ranges_list))
    # sleep 5 seconds
    time.sleep(5)
    # for dataset_data in dataset_list:
    for [index, dataset_data] in enumerate(dataset_list):
        print(f"""Loading.....{dataset_data["name"]}""")
        dataset_name=dataset_data["name"]
        # Load Dataset
        dataset = load_dataset(dataset_name, split="train")
        dataset_list[index]["dataset"]=dataset
        print(f"""Dataset {dataset_name} loaded successfully.""")
        print(f"""Total Length: {len(dataset)}""")
    for selectRange in tqdm(ranges_list, desc="Processing Range"):
        all_sentences=[]
        all_words=[]
        all_mix=[]
    # Loop through dataset_name_list and run extract_sentences(dataset)
        # for dataset_data in dataset_list:
        for [index, dataset_data] in enumerate(dataset_list):
            dataset = dataset_list[index]["dataset"]            
            column_name=dataset_data["column"]
            # Print all the column names in the dataset
            # print(dataset["train"].column_names)            
            sentences, words, mix = extract_sentences(dataset.select(selectRange),sample_size,dataset_name,column_name)
            all_sentences = all_sentences + sentences
            all_words = all_words + words
            all_mix = all_mix + mix

            random.shuffle(all_sentences)
            random.shuffle(all_words)
            random.shuffle(all_mix)
            
        print(f"""Total sentences: {len(all_sentences)}""")
        print(f"""Total words: {len(all_words)}""")
        print(f"""Total mix: {len(all_mix)}""")

        # Truncate the sentences list to the first 50 sentences
        all_sentences = all_sentences[:100]
        all_words = all_words[:150]
        all_mix = all_mix[:150]
        saveToFile(f"all_sentences","",all_sentences)
        saveToFile(f"all_words","",all_words)
        saveToFile(f"all_mix","",all_mix)
        notes.append(all_sentences)
        notes.append(all_words)
        notes.append(all_mix)

    # Create a dataset with the "notes" column
    dataset_combined = Dataset.from_dict({"notes": notes})

    # Save the dataset to local disk
    dataset_combined.save_to_disk("./mixer_dataset_combined_20k")

    print("Combined dataset saved successfully.")
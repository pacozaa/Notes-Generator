import time
from datasets import load_dataset, Dataset
from tqdm import tqdm
from generator.hot_topics import generate_hot_topics
from generator.department import generate_departments
# Add new columns for HotTopics and Department
def process_dataset(dataset):
    new_rows = []
    hot_topics = []
    departments = []
    # Use tqdm to wrap the extracted_data iterable
    # for row in tqdm(extracted_data, desc="Processing rows"):
    for row in tqdm(dataset, desc="Processing rows"):  # Assuming we are working with the 'train' split
        try:
            description = row["description"]
            companyName = row["companyName"]
            hot_topics = generate_hot_topics(companyName,description)
            departments = generate_departments(companyName,description)
            hot_topics = eval(hot_topics)["hotTopics"]
            departments = eval(departments)["departments"]

        except Exception as e:
            print(f"Error parsing response: {e}")


        row["hotTopics"] = hot_topics
        row["departments"] = departments
        
        # sleep 300ms
        
        # time.sleep(0.3)
        new_rows.append(row)
    # Convert the list of new rows back into a Dataset object
    updated_dataset = Dataset.from_list(new_rows)
    return updated_dataset



# main function
if __name__ == "__main__":
    # Load the dataset
    dataset_name="pacozaa/tech-company-news-data-dump-clean"
    dataset = load_dataset(dataset_name,split="train")
    dataset = dataset.select(range(1000,len(dataset)))
    # Apply the process
    updated_dataset = process_dataset(dataset)

    # Specify the local directory where you want to save the dataset
    local_path = "./updated_dataset-1000-MAX"

    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)
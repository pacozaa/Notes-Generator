import os
import json
from datasets import load_dataset

def read_json_files_in_directory(directory):
    # List to store the contents of all JSON files
    json_data = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)

            # Open and read the JSON file
            with open(file_path, 'r') as file:
                try:
                    # Load the JSON data
                    data = json.load(file)
                    # Append the data to the list
                    json_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {file_path}: {e}")

    return json_data

def write_jsonl_file(data, output_file):
    with open(output_file, 'w') as file:
        for item in data:
            for entry in item:
                json.dump(entry, file)
                file.write('\n')



# main
if __name__ == "__main__":
    # Example usage
    directory_path = './data-json'
    output_file = './dataset/merged_data.jsonl'
    all_json_data = read_json_files_in_directory(directory_path)


    # Print the updated contents of all JSON data
    for data in all_json_data:
        print(data)

    # Write the merged data to a JSONL file
    write_jsonl_file(all_json_data, output_file)
    dataset = load_dataset('json', data_files='./dataset/merged_data.jsonl')
    # Print the dataset to verify
    print(dataset)
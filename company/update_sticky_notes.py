import time
from datasets import load_dataset, Dataset
from tqdm import tqdm
# Add the project root to the Python path
import sys
import os
import random
# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to the Python path
sys.path.append(project_root)
from generator.sticky_note import generate_sticky_notes

def map_dataset_with_sticky_notes(examples):
    companyName = examples["companyName"]
    description = examples["description"]
    hotTopics = examples["hotTopics"]
    departments = examples["departments"]
    sticky_notes = []
    meeting_names = []
    for companyName, description, hotTopic, department in zip(companyName, description, hotTopics, departments):        
        try:
            # hotTopic[:1], department[:1] to get the first element of the list
            # hotTopic, department to get the full list
            # hotTopic[1], department[1] to get the second element of the list
            # hotTopic[2], department[2] to get the third element of the list
            selected_hotTopic=random.choice(hotTopic)
            selected_department=random.choice(department)
            response = generate_sticky_notes(companyName, description, selected_hotTopic, selected_department)
            sticky_note = eval(response)["stickyNotes"]
            meeting_name = eval(response)["meetingName"]
            print(sticky_note)
            print(meeting_name)
            sticky_notes.append(sticky_note)
            meeting_names.append(meeting_name)
            return {"stickyNotes": sticky_notes, "meetingName": meeting_names}
        except Exception as e:
            print(f"Error parsing response: {e}")
            sticky_notes.append([])
            meeting_names.append("")
            return {"stickyNotes": sticky_notes, "meetingName": meeting_names}
    # print(f"Generated sticky notes length: {len(sticky_notes)}")
    

# main function
if __name__ == "__main__":
    # Load the dataset
    dataset_name="pacozaa/company_v2"
    dataset = load_dataset(dataset_name,split="train")
    dataset = dataset.shuffle().select(range(700,800))
    # Apply the process
    updated_dataset = dataset.map(
        map_dataset_with_sticky_notes, batched=True, batch_size=1, load_from_cache_file=False)

    # Specify the local directory where you want to save the dataset
    local_path = "./dataset/ollama/updated_sticky_notes_700_800_runpod_ollama_random"

    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)
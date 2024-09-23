import time
from synthetic_detail import generate_synthetic_sticky_notes
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
    llm_responses=[]
    all_details = []
    for companyName, description, hotTopic, department in zip(companyName, description, hotTopics, departments):  
        llm_response = ""      
        selected_hotTopic=random.choice(hotTopic)
        selected_department=random.choice(department)
        more_info = generate_synthetic_sticky_notes()
        all_detail = f"""
Company Name: {companyName}
Description: {description}
hot topics: {selected_hotTopic}
Departments: {selected_department}
{more_info}
"""
        all_details.append(all_detail)
        try:
            
            llm_response = generate_sticky_notes(companyName, description, selected_hotTopic, selected_department, more_info)
            llm_responses.append(llm_response)
            
            sticky_note = eval(llm_response)["stickyNotes"]
            meeting_name = eval(llm_response)["meetingName"]
            # print(sticky_note)
            # print(meeting_name)
            sticky_notes.append(sticky_note)
            meeting_names.append(meeting_name)
            # return {"stickyNotes": sticky_notes, "meetingName": meeting_names, "llm_response":llm_responses}
        except Exception as e:
            print(f"Error parsing response: {e}")
            llm_responses.append(llm_response)
            sticky_notes.append([])
            meeting_names.append("")
            # return {"stickyNotes": sticky_notes, "meetingName": meeting_names, "llm_response":llm_responses}
    
    # Return the full batch results (length should match the batch size)
    return {"stickyNotes": sticky_notes, "meetingName": meeting_names, "llm_response": llm_responses, "all_detail":all_details}
    

# main function
if __name__ == "__main__":
    # Load the dataset
    dataset_name="pacozaa/company_v2"
    dataset = load_dataset(dataset_name,split="train")
    dataset = dataset.shuffle().select(range(2500,2800))
    # Apply the process
    updated_dataset = dataset.map(
        map_dataset_with_sticky_notes, batched=True, batch_size=10, load_from_cache_file=False)

    # Specify the local directory where you want to save the dataset
    local_path = "./dataset/sticky_notes/2500_2800_4o"

    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)
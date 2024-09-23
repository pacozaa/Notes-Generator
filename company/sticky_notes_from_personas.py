import time
import uuid
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
from generator.sticky_note_from_persona import generate_sticky_notes_from_persona
from meeting_frameworks import meeting_frameworks_names

def map_dataset_with_sticky_notes(examples):
    personas = examples["persona"]
    sticky_notes = []
    discussion_names = []
    llm_responses=[]
    frameworks=[]
    for persona in zip(personas):  
        llm_response = ""
        meeting_frameworks_name=random.choice(meeting_frameworks_names)
        frameworks.append(meeting_frameworks_name)
        try:
            llm_response = generate_sticky_notes_from_persona(persona, meeting_frameworks_name)
            llm_responses.append(llm_response)
            
            sticky_note = eval(llm_response)["stickyNotes"]
            discussion_name = eval(llm_response)["discussionName"]
            # print(sticky_note)
            # print(meeting_name)
            sticky_notes.append(sticky_note)
            discussion_names.append(discussion_name)
            
        except Exception as e:
            print(f"Error parsing response: {e}")
            llm_responses.append(llm_response)
            sticky_notes.append([])
            discussion_names.append("")
    
    # Return the full batch results (length should match the batch size)
    return {"stickyNotes": sticky_notes, "discussionName": discussion_names, "llm_response": llm_responses,"framework":frameworks}
    

# main function
if __name__ == "__main__":
    # Load the dataset
    # pacozaa/TeamPersonaHub_business_3_300k
    # pacozaa/persona_mixed_7_300k
    # pacozaa/fine_persona_mixed_7_300k
    dataset_name="pacozaa/TeamPersonaHub_business_3_300k"
    dataset = load_dataset(dataset_name,split="train")
    dataset = dataset.shuffle().select(range(300))
    # Apply the process
    updated_dataset = dataset.map(
        map_dataset_with_sticky_notes, batched=True, batch_size=10, load_from_cache_file=False)

    # Specify the local directory where you want to save the dataset
    local_path = f"./dataset/sticky_notes/TeamPersonaHub_business_4o_{str(uuid.uuid4())}"

    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)
import uuid
from datasets import load_dataset
from openai import OpenAI
from dotenv import load_dotenv
import random
from conversation.synthetic_detail import styles, tones, desired_lengths, categories
from conversation.prompts import get_conversation_prompt
# Load environment variables from .env file
load_dotenv()
import os
client = OpenAI(
    # base_url="https://api.groq.com/openai/v1",
    # api_key=os.environ.get("GROQ_API_KEY")
    api_key=os.environ.get("OPENAI_API_KEY")

)
# model="llama-3.3-70b-versatile"
model="gpt-4o-mini"

def llm_generate_conversation(persona_1,persona_2, tone, desired_length, style):    
    """
    Generates a conversation between two personas using a language model.
    Args:
        persona_1 (str): The first persona's description.
        persona_2 (str): The second persona's description.
        tone (str): The tone of the conversation (e.g., formal, casual).
        desired_length (int): The desired length of the conversation.
        style (str): The style of the conversation (e.g., narrative, dialogue).
    Returns:
        str: The generated conversation content.
    """
    print({
        "persona_list0": persona_1,
        "persona_list1": persona_2,
        "tone": tone,
        "desired_length": desired_length,
        "style": style
    })
    completion = client.chat.completions.create(
        model=model,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": get_conversation_prompt(persona_1,persona_2, tone, desired_length, style)
            }
        ]
    )

    # print(completion.choices[0].message)
    return completion.choices[0].message.content

def map_dataset_with_conversation(examples):
    personas = examples["persona"]
    llm_responses=[]
    selected_personas_1=[]
    selected_personas_2=[]
    selected_tones=[]
    selected_desired_lengths=[]
    selected_styles=[]
    for persona in zip(personas):  
        llm_response = ""
        selected_persona_1=persona[0][0]
        selected_persona_2=persona[0][1]
        selected_tone=random.choice(tones)
        selected_desired_length=random.choice(desired_lengths)
        selected_style=random.choice(styles)
        try:
            llm_response = llm_generate_conversation(selected_persona_1,selected_persona_2, selected_tone, selected_desired_length, selected_style)
            llm_responses.append(llm_response)
            selected_personas_1.append(persona[0][0])
            selected_personas_2.append(persona[0][1])
            selected_tones.append(random.choice(tones))
            selected_desired_lengths.append(random.choice(desired_lengths))
            selected_styles.append(random.choice(styles))
            # print(llm_response)
            
        except Exception as e:
            print(f"Error parsing response: {e}")
            llm_responses.append(llm_response)
    
    # Return the full batch results (length should match the batch size)
    return {"llm_response": llm_responses, "persona_1": selected_personas_1, "persona_2": selected_personas_2, "tone": selected_tones, "desired_length": selected_desired_lengths, "style": selected_styles}

def main():
    # Load the dataset
    # pacozaa/TeamPersonaHub_business_3_300k
    # pacozaa/persona_mixed_7_300k
    # pacozaa/fine_persona_mixed_7_300k
    size=50
    dataset_name="pacozaa/TeamPersonaHub_business_3_300k"
    dataset = load_dataset(dataset_name,split="train")
    dataset = dataset.shuffle().select(range(size))
    # Apply the process
    updated_dataset = dataset.map(
        map_dataset_with_conversation, batched=True, batch_size=10, load_from_cache_file=False)#, load_from_cache_file=False

    # Specify the local directory where you want to save the dataset
    local_path = f"./dataset/conversations/TeamPersonaHub_Conversations_{model}_{str(uuid.uuid4())}"
    print(local_path)
    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)

if __name__ == "__main__":
    main()
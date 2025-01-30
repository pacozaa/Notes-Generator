import uuid
from datasets import load_dataset
from openai import OpenAI
from dotenv import load_dotenv
import random
from email.synthetic_detail import investmentExperience, emailLength, clientPersona, brokerStyle, marketConditions, investmentTopics, clientExperience, urgency, structureOfConversation
from email.prompts import get_email_prompt
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

def llm_generate_email(
        character, 
        investment_experience, 
        email_length, 
        client_persona, 
        broker_style, 
        market_conditions, 
        investment_topics, 
        urgency, 
        structure_of_conversation
    ):    
    
    completion = client.chat.completions.create(
        model=model,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": get_email_prompt(
                    character, 
                    investment_experience, 
                    email_length, 
                    client_persona, 
                    broker_style, 
                    market_conditions, 
                    investment_topics, 
                    urgency, 
                    structure_of_conversation)
            }
        ]
    )

    # print(completion.choices[0].message)
    return completion.choices[0].message.content

def map_dataset_with_email(examples):
    personas = examples["persona"]
    llm_responses=[]
    selected_characters=[]
    selected_investment_experiences=[]
    selected_email_lengths=[]
    selected_client_personas=[]
    selected_broker_styles=[]
    selected_market_conditions=[]
    selected_investment_topics=[]
    selected_client_experiences=[]
    selected_urgencies=[]
    selected_structure_of_conversations=[]

    for persona in zip(personas):  
        llm_response = ""
        selected_character=persona[0]
        selected_investment_experience=random.choice(investmentExperience)
        selected_email_length=random.choice(emailLength)
        selected_client_persona=random.choice(clientPersona)
        selected_broker_style=random.choice(brokerStyle)
        selected_market_condition=random.choice(marketConditions)
        selected_investment_topic=random.choice(investmentTopics)
        selected_client_experience=random.choice(clientExperience)
        selected_urgency=random.choice(urgency)
        selected_structure_of_conversation=random.choice(structureOfConversation)
        
        print("character: "+selected_character)
        try:
            llm_response = llm_generate_email(
                selected_character, 
                selected_investment_experience, 
                selected_email_length, 
                selected_client_persona, 
                selected_broker_style, 
                selected_market_condition, 
                selected_investment_topic,
                selected_urgency, 
                selected_structure_of_conversation
            )
            llm_responses.append(llm_response)
            selected_characters.append(selected_character)
            selected_investment_experiences.append(selected_investment_experience)
            selected_email_lengths.append(selected_email_length)
            selected_client_personas.append(selected_client_persona)
            selected_broker_styles.append(selected_broker_style)
            selected_market_conditions.append(selected_market_condition)
            selected_investment_topics.append(selected_investment_topic)
            selected_client_experiences.append(selected_client_experience)
            selected_urgencies.append(selected_urgency)
            selected_structure_of_conversations.append(selected_structure_of_conversation)
            # print(llm_response)
            
        except Exception as e:
            print(f"Error parsing response: {e}")
            llm_responses.append(llm_response)
    
    # Return the full batch results (length should match the batch size)
    return {
        "llm_response": llm_responses, 
        "character":selected_characters, 
        "investment_experience":selected_investment_experiences, 
        "email_length":selected_email_lengths, 
        "client_persona":selected_client_personas,
        "broker_style":selected_broker_styles, 
        "market_condition":selected_market_conditions, 
        "investment_topic":selected_investment_topics, 
        "client_experience":selected_client_experiences, 
        "urgency":selected_urgencies, 
        "structure_of_conversation":selected_structure_of_conversations
            }

def main():
    # Load the dataset
    # pacozaa/TeamPersonaHub_business_3_300k
    # proj-persona/PersonaHub ,subset "persona", split="train"
    size=150
    dataset_name="proj-persona/PersonaHub"
    dataset = load_dataset(dataset_name,"persona",split="train")
    dataset = dataset.shuffle().select(range(size))
    # Apply the process
    updated_dataset = dataset.map(
        map_dataset_with_email, batched=True, batch_size=10, load_from_cache_file=True)#, load_from_cache_file=False

    # Specify the local directory where you want to save the dataset
    local_path = f"./dataset/emails/PersonaHub_emails_{size}_{model}_{str(uuid.uuid4())}"
    print(local_path)
    # Save the dataset to the local directory
    updated_dataset.save_to_disk(local_path)

if __name__ == "__main__":
    main()
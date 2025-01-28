
def get_conversation_prompt(character_1, character_2, tone, desired_length, styles):
    """
    Generates a prompt for creating a synthetic conversation between two characters.

    Args:
        character_1 (str): The name or identifier of the first character.
        character_2 (str): The name or identifier of the second character.
        tone (str): The tone of the conversation (e.g., formal, casual, humorous, professional).
        topic (str): The topic around which the conversation should be centered.
        desired_length (str): The desired length of the conversation (e.g., short 5 exchanges or long 10 exchanges).
        styles (str): The distinct speaking styles of the participants.

    Returns:
        str: A formatted prompt string for generating the conversation.
    """
    prompt =f"""You are a professional scriptwriter tasked with creating a synthetic conversation between {character_1} and {character_2}. The conversation should:
- Tone: Follow a {tone} tone (e.g., formal, casual, humorous, professional).
- Desired Length: Have a {desired_length}
- Style: The participants should have distinct speaking styles: {styles}.

Generate the conversation as follows:
Topic: [concise topic]
{character_1}: [line]
{character_2}: [response]
Continue until the end of the conversation.
"""
    # print(prompt)
    return prompt

def verify_conversation_prompt(tone, topic, style, conversation):
    prompt = f"""You are an LLM trained to evaluate synthetic conversations. Your task is to verify if the generated conversation meets the following criteria:
1. Adheres to the specified tone: {tone}.
2. Stays relevant to the topic: {topic}.
3. Matches the distinct speaking styles for each participant: {style}.
4. Has no factual inconsistencies or grammar errors.

Here is the conversation to evaluate:
{conversation}

Evaluate the conversation and return:
- "Pass" if it meets all criteria.
- A list of issues if it fails, with corrections or suggestions.
"""
    return prompt

# character, 
# investmentExperience, 
# emailLength, 
# clientPersona, 
# brokerStyle, 
# marketConditions, 
# investmentTopics, 
# urgency, 
# structureOfConversation
def get_email_prompt(
        character, 
        investment_experience, 
        length,
        client_persona,
        broker_style,
        market_condition,
        investment_topic, 
        urgency,
        structure_of_conversation):
    """
    Generates a prompt for creating a realistic email thread between a stockbroker and a client.

    Args:
        character (str): The persona or background of the client (e.g., "a cautious retiree" or "a young tech entrepreneur").
        investment_experience (str): The client's level of investment experience (e.g., "beginner", "intermediate", "expert").
        urgency (str): The urgency or tone of the conversation (e.g., "calm and informative", "urgent and persuasive").
        length (str): The desired length of the email thread (e.g., "short", "medium", "long").
        broker_style (str): The stockbroker's communication style (e.g., "formal and professional", "casual and friendly").
        market_condition (str): The current state of the market (e.g., "volatile", "bullish", "bearish").
        investment_topic (str): The main topic of discussion (e.g., "tech stocks", "retirement planning").
        structure_of_conversation (str): Additional instructions for structuring the conversation (e.g., "include follow-up questions", "ensure a decisive conclusion").

    Returns:
        str: A formatted prompt describing the characteristics of the email thread.
    """
    prompt = f"""Generate a realistic email thread between a stockbroker and a client. The email thread should be {length} in length. 

The client is {character} and also {client_persona} who has {investment_experience} level of experience in investing. The broker's communication style is {broker_style}. The current market condition is {market_condition}, and the discussion revolves around {investment_topic}. 

Ensure that the broker provides insights and suggestions while maintaining a {urgency} tone. The client should respond in a way that aligns with their persona, experience, and concerns. 

Structure the conversation naturally with appropriate greetings, sign-offs, and follow-ups. Vary email lengths for realism and the overall structure of conversation should be {structure_of_conversation}. """
    # print(prompt)
    return prompt
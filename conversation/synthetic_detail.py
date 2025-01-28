import random
# This is a conversation synthetic data generator helper function

categories = [
    "UNKNOWN","TECHNOLOGY","FINANCE","MARKETING","SALES","HR","LEGAL","OPERATIONS","PRODUCT","CUSTOMER SERVICE","RESEARCH","MANAGEMENT"
]

tones = [ "Formal", "Casual", "Humorous", "Serious", "Inspirational", "Argumentative", 
    "Empathetic", "Neutral", "Romantic", "Sarcastic", "Mystical", "Technical"]


# 1. **Very Short**: 3-4 exchanges (e.g., quick Q&A).
# 2. **Short**: 5-7 exchanges (e.g., brief interaction or concise dialogue).
# 3. **Medium**: 8-12 exchanges (e.g., detailed conversation or scenario).
# 4. **Long**: 13-20 exchanges (e.g., full discussion or scene development).
# 5. **Very Long**: 20+ exchanges (e.g., in-depth debate or storytelling).
desired_lengths = [ "Very Short: 3-4 exchanges (e.g., quick Q&A)", 
"Short: 5-7 exchanges (e.g., brief interaction or concise dialogue).", 
"Medium: 8-12 exchanges (e.g., detailed conversation or scenario).", 
"Long: 13-20 exchanges (e.g., full discussion or scene development).", 
"Very Long: 20+ exchanges (e.g., in-depth debate or storytelling)."]

styles = [ "Friendly", "Professional", "Academic", "Persuasive", "Storytelling", 
    "Role-playing", "Q&A", "Philosophical", "Mystery", "Explanatory", 
    "Debate", "Playful", "Customer Service", "Historical", "Fantasy"]
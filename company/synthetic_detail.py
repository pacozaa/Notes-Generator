import random
import json
from meeting_frameworks import meeting_frameworks_names
# Define components to mix
categories = [
    "UNKNOWN","To-Do", "Meeting Notes", "Ideas", "Reminder", "Project Milestones", "Feedback", "Decisions", "Action Items","Deadlines"
]

priorities = [
    "UNKNOWN","High", "Medium", "Low"
]

styles = [
    "UNKNOWN","Formal", "Casual", "Bullet Points", "Shorthand"
]

meeting_types = [
    "UNKNOWN", "Informal", "Formal", "Interactive", "Structured", "Unstructured", "Visual", "Textual", "Hybrid"
    "Stand-up Meeting", "Brainstorming Session", "One-on-One Meeting", "Team Meeting", 
    "Project Kickoff Meeting", "Status Update Meeting", "Decision-Making Meeting", 
    "Client Meeting", "Retrospective Meeting", "All-Hands Meeting", "Problem-Solving Meeting",
    "Performance Review Meeting", "Training Session", "Workshops", "Check-In Meeting", 
    "Town Hall Meeting", "Board Meeting", "Strategy Session", "Weekly Sync Meeting", 
    "Design Review Meeting"
]

# Function to generate synthetic sticky notes
def generate_synthetic_sticky_notes():
    # Randomly select components
    category = random.choice(categories)
    priority = random.choice(priorities)
    style = random.choice(styles)
    framework = random.choice(meeting_frameworks_names)
    meeting_type = random.choice(meeting_types)
    
    consolidate_text = f"""\nTheme: {category}\nPriority: {priority}\nStyle: {style}\nFramework: {framework}\nMeeting Type: {meeting_type}"""
    # print(f"""Synthetic Detail:\n{consolidate_text}""")
    return consolidate_text
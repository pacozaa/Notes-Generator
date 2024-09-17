def get_hot_topics_prompt(company_name, company_description):
  prompt = f"""Generate 5 hot topics for this company name
Name: {company_name}
Description: {company_description}

Output only valid compact JSON in JSON array of string"""
  return prompt

def get_departments_prompt(company_name, company_description):
  prompt = f"""Generate 7 departments for this company name
Name: {company_name}
Description: {company_description}

Output only valid compact JSON in JSON array of string"""
  return prompt

def get_sticky_note_system_prompt():
    prompt = """You are a company hot topics generator.
The Output JSON schema should include:
{ 
"meetingName": string(name of the meeting),
"stickyNotes":[array of string(content of sticky notes used in the meeting)]
}"""
    return prompt

def get_sticky_note_prompt(company_name, company_description,hot_topics,departments):
  prompt = f"""Generate meeting name and 20 sticky notes based on this information
Company Name: {company_name}
Description: {company_description}
hot topics: {hot_topics}
Departments: {departments}

The Output JSON schema should include:
{{ 
"meetingName": string(name of the meeting),
"stickyNotes":[array of string(content of sticky notes used in the meeting)]
}}"""
  # print(prompt)
  return prompt

# {
#   "meetingName": "Gold Investment Strategies at A-Mark Precious Metals",
#   "stickyNotes": [
#     "Discuss the advantages of purchasing physical gold versus gold funds.",
#     "Explore current trends in the gold market.",
#     "Client feedback on gold investment options.",
#     "A-Mark's role in facilitating gold investments.",
#     "Best practices for navigating gold investments.",
#     "Risks associated with investing in physical gold vs. funds.",
#     "Competitor analysis in the gold market.",
#     "Educational resources for clients on gold investing.",
#     "Key takeaways from industry research on gold.",
#     "Investment strategies tailored for different client profiles.",
#     "Data analysis on gold price fluctuations.",
#     "Building a reliable gold portfolio for clients.",
#     "Impacts of geopolitical news on gold prices.",
#     "Application of risk management in gold trading.",
#     "Enhancing client relations through gold market insights.",
#     "Leveraging technology in gold transactions.",
#     "Marketing strategies for promoting gold investment services.",
#     "Cross-department collaboration on gold-related projects.",
#     "Feedback loop: How can we improve our gold buying guide?",
#     "Identifying target demographics for gold investments.",
#     "Action items for upcoming gold market presentations."
#   ]
# }
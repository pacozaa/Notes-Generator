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
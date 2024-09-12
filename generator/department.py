from generator.prompts import get_departments_prompt
from llm.openai import client
from llm.openai import model

def get_departments_prompt(company_name, company_description):
  prompt = f"""Generate 7 departments for this company name
Name: {company_name}
Description: {company_description}

Output only valid compact JSON in JSON array of string"""
  return prompt

def generate_departments(company_name, company_description):
  
  completion = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "system",
              "content": """You are a company departments name generator
The Output JSON schema should include:
{ 
"departments": [array of string(name of the departments)]
}
"""
          },
          {
              "role": "user",
              "content": get_departments_prompt("10Clouds","Uber HP and more in the latest Market Talks covering Technology Media and Telecom.")
          },
          {
              "role": "assistant",
              "content":"""{"departments":[
  "Market Research",
  "Product Development",
  "Marketing Communications",
  "Client Success",
  "Market Insights",
  "Technology Solutions",
  "UX/UI Design"
]}"""
          },
          {
              "role": "user",
              "content": get_departments_prompt("3ilogics","The Ithaca City School District has launched a mobile app alongside updates to its website ahead of the upcoming 2023 - 2024 school year.")
          },
          {
              "role": "assistant",
              "content":"""{"departments":[
  "Application Development",
  "Digital Infrastructure",
  "Cybersecurity",
  "Database Management",
  "Network Services",
  "Software Quality Assurance",
  "IT Support Services"
]}"""
          },
          {
              "role": "user",
              "content": get_departments_prompt(company_name,company_description)
          }
      ],
      temperature=0.5,
      max_tokens=1024,
      top_p=0.65,
      stream=False,
      stop=None,
      response_format = {"type": "json_object"} 
  )

  # print(completion.choices[0].message)
  return completion.choices[0].message.content


from generator.prompts import get_hot_topics_prompt
from llm.openai import client
from llm.openai import model
def generate_hot_topics(company_name, company_description):
  
  completion = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "system",
              "content": """You are a company hot topics generator.
The Output JSON schema should include:
{ 
"hotTopics": [array of string(name of the hot topics)]
}
"""
          },
          {
              "role": "user",
              "content": get_hot_topics_prompt("10Clouds","Uber HP and more in the latest Market Talks covering Technology Media and Telecom.")
          },
          {
              "role": "assistant",
              "content": """{"hotTopics":[
  "10Clouds' Innovative Solutions in Technology, Media, and Telecom",
  "Market Talks: Uber HP and Beyond",
  "The Future of Technology with 10Clouds",
  "10Clouds' Impact on the Media and Telecom Industry",
  "Inside 10Clouds: Transforming the Tech Landscape"
]}"""
          },
          {
              "role": "user",
              "content": get_hot_topics_prompt("3ilogics","The Ithaca City School District has launched a mobile app alongside updates to its website ahead of the upcoming 2023 - 2024 school year.")
          },
          {
              "role": "assistant",
              "content": """{"hotTopics":[
  "3ilogics' Role in the Ithaca City School District's Digital Transformation",
  "The Future of Education: How 3ilogics is Enhancing Learning Experiences",
  "3ilogics' Innovative Solutions for School Districts",
  "Ithaca City School District's Mobile App and Website Updates: A 3ilogics Partnership",
  "Behind the Scenes of 3ilogics: Revolutionizing Education with Technology"
]}"""
          },
          {
              "role": "user",
              "content": get_hot_topics_prompt(company_name, company_description)
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
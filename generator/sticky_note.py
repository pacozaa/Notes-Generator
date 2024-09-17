from generator.prompts import get_sticky_note_system_prompt, get_sticky_note_prompt
from llm.openai import client
from llm.openai import model
import time
def generate_sticky_notes(company_name, company_description,hot_topics,departments):
  start_time = time.time()
  completion = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "system",
              "content": get_sticky_note_system_prompt()
          },
          {
              "role": "user",
              "content": get_sticky_note_prompt(
                "Actalent",
                """A driverless car company operating in San Francisco 
and a company that supplied it human test drivers have taken a dispute over 
who should pay for an accident to federal court.""",
", ".join([ "Actalent's Role in the Driverless Car Industry Dispute", "The Future of Autonomous Vehicles: Actalent's Expertise", "Actalent's Human Test Drivers at the Center of a High-Stakes Lawsuit", "Driverless Car Company vs. Test Driver Supplier: Actalent's Involvement", "The Actalent Advantage: Navigating the Complexities of Autonomous Transportation" ]
),
", ".join([ "Autonomous Systems", "Risk Management", "Regulatory Compliance", "Human Resources", "Test Operations", "Safety Engineering", "Litigation Support" ])
)
          },
          {
              "role": "assistant",
              "content": """{
  "meetingName": "Navigating the Actalent Litigation: Strategies and Insights",
  "stickyNotes": [
    "Overview of the ongoing federal court dispute.",
    "Implications of the lawsuit for Actalent's operations.",
    "Understanding the roles of autonomous systems and human test drivers.",
    "Key evidence and documentation needed for litigation support.",
    "Risk management strategies for future driverless car projects.",
    "Regulatory compliance steps to mitigate legal risks.",
    "Internal training for human test drivers regarding legal liability.",
    "Updates on industry standards impacting autonomous vehicles.",
    "Communication plan for stakeholders regarding the lawsuit.",
    "Monitor public perception regarding the dispute.",
    "Collaborate with legal experts for comprehensive defense.",
    "Safety engineering assessments related to the accident.",
    "Discuss potential outcomes of the litigation process.",
    "Human resources policies for supporting affected test drivers.",
    "Strategy for future autonomous system development amidst legal challenges.",
    "Best practices for crisis management in high-stakes lawsuits.",
    "Feedback from test operations on safety protocols.",
    "Identify lessons learned from the dispute for future projects.",
    "Evaluate financial implications of the ongoing lawsuit.",
    "Engagement with the media regarding Actalent's position.",
    "Next steps following the court hearings."
  ]
}"""
          },
          {
              "role": "user",
              "content": get_sticky_note_prompt(
                "A-Mark Precious Metals",
                """There are two main ways to buy gold: 
purchasing physical gold or investing via a financial instrument like funds.""",
", ".join([ "A-Mark Precious Metals: Your Guide to Buying Gold", "Physical Gold vs. Gold Funds: A-Mark Precious Metals Weighs In", "Investing in Gold: A-Mark Precious Metals' Expert Insights", "A-Mark Precious Metals: Your Trusted Source for Gold Investments", "Navigating the Gold Market: A-Mark Precious Metals' Expert Advice" ]),
", ".join([ "Precious Metals Trading", "Investment Services", "Financial Analysis", "Risk Management", "Commodity Research", "Client Relations", "Market Operations" ])
)
          },
          {
              "role": "assistant",
              "content": """{
  "meetingName": "Gold Investment Strategies at A-Mark Precious Metals",
  "stickyNotes": [
    "Discuss the advantages of purchasing physical gold versus gold funds.",
    "Explore current trends in the gold market.",
    "Client feedback on gold investment options.",
    "A-Mark's role in facilitating gold investments.",
    "Best practices for navigating gold investments.",
    "Risks associated with investing in physical gold vs. funds.",
    "Competitor analysis in the gold market.",
    "Educational resources for clients on gold investing.",
    "Key takeaways from industry research on gold.",
    "Investment strategies tailored for different client profiles.",
    "Data analysis on gold price fluctuations.",
    "Building a reliable gold portfolio for clients.",
    "Impacts of geopolitical news on gold prices.",
    "Application of risk management in gold trading.",
    "Enhancing client relations through gold market insights.",
    "Leveraging technology in gold transactions.",
    "Marketing strategies for promoting gold investment services.",
    "Cross-department collaboration on gold-related projects.",
    "Feedback loop: How can we improve our gold buying guide?",
    "Identifying target demographics for gold investments.",
    "Action items for upcoming gold market presentations."
  ]
}"""
          },
          {
              "role": "user",
              "content": get_sticky_note_prompt(company_name, company_description,hot_topics,departments)
          }
      ],
      temperature=0.5,
      max_tokens=1024,
      top_p=0.65,
      stream=True,
      stop=None,
      response_format = {"type": "json_object"} 
  )

  
  # return completion.choices[0].message.content
  collected_chunks = []
  collected_messages = []
  # iterate through the stream of events
  for chunk in completion:
      chunk_time = time.time() - start_time  # calculate the time delay of the chunk
      collected_chunks.append(chunk)  # save the event response
      chunk_message = chunk.choices[0].delta.content  # extract the message
      collected_messages.append(chunk_message)  # save the message
      print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

  # print the time delay and text received
  print(f"Full response received {chunk_time:.2f} seconds after request")
  # clean None in collected_messages
  collected_messages = [m for m in collected_messages if m is not None]
  full_reply_content = ''.join(collected_messages)
  print(f"Full conversation received: {full_reply_content}")
  return full_reply_content
from generator.prompts import get_sticky_note_from_persona_system_prompt, get_sticky_note_from_persona_prompt
from llm.openai import client
from llm.openai import model
# from llm.groq import client
# from llm.groq import model
import time
def generate_sticky_notes_from_persona(persona_list,meeting_frameworks_name):
  start_time = time.time()
  completion = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "system",
              "content": get_sticky_note_from_persona_system_prompt()
          },
          {
              "role": "user",
              "content": get_sticky_note_from_persona_prompt(persona_list,meeting_frameworks_name)
          }
      ],
      temperature=0.5,
      max_tokens=1024,
      top_p=0.65,
      # stream=True,
      stop=None,
      response_format = {"type": "json_object"} 
  )

  
  return completion.choices[0].message.content
  if False:
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
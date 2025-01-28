from llm.openai import client
from llm.openai import model

def send_message(message):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stop=None
    )
    return completion.choices[0].message.content

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: chat <message>")
        sys.exit(1)

    message = " ".join(sys.argv[1:])
    response = send_message(message)
    print(response)

if __name__ == "__main__":
    main()
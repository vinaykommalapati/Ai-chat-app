import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and friendly AI assistant. Be concise and clear in your responses."
            }
        ] + conversation_history,
        max_tokens=1024
    )

    assistant_message = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    print("=" * 50)
    print("   AI Chat App — Built by Vinay Kommalapati")
    print("=" * 50)
    print("Type your message and press Enter to chat.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! 👋")
            break

        print("AI: Thinking...", end="\r")
        response = chat(user_input)
        print(f"AI: {response}\n")


if __name__ == "__main__":
    main()

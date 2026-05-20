from openai import OpenAI
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)  # set OPENAI_API_KEY in your environment

while True:
    question = input("Ask a Salesforce question: ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Salesforce expert."},
        {"role": "user", "content": question}
    ]
    )

    print(response.choices[0].message.content)

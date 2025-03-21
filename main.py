from langchain_ollama  import OllamaLLM
from langchain_core .prompts import ChatPromptTemplate

template = """
answer the following questions
here is the conversation context:{conversation_context}
Question: {question}
Example : {example}
Answer: 
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt|model
# Assuming this is the relevant part of your main.py
result = chain.invoke({
    'conversation_context': 'asking you tips to get better at programming and build the brain muscles for thinking like a programmer',
    'question': 'how to get better at programming?',  # Changed 'Question' to 'question'
    'example': ''
})


def continuous_conversation():
    conversation_history = []

    print("Start chatting with the model! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Ending conversation. Goodbye!")
            break

        # Generate a response from the model
        result = chain.invoke({
            'conversation_context': 'ongoing conversation',
            'question': user_input,
            'example': ''
        })

        # Store the conversation in history
        conversation_history.append({"user": user_input, "model": result})

        # Print the model's response
        print(f"Model: {result}")

    # Optionally, you can save the conversation history to a file
    with open("conversation_history.txt", "w") as file:
        for entry in conversation_history:
            file.write(f"You: {entry['user']}\n")
            file.write(f"Model: {entry['model']}\n\n")

if __name__ == "__main__":
    continuous_conversation()
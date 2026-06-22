from app.llm import answer_question

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    print(answer_question(question))



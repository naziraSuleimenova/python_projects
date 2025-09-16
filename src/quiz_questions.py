from Question import Question

question_prompts = [
    "What is the capital of Canada?\n(a) Vancouver\n(b) Ottawa\n(c) Montreal\n\n",
    "What is the capital of Australia?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n\n",
    "What is the capital of Brazil?\n(a) Rio de Janeiro\n(b) São Paulo\n(c) Brasília\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Nope\n")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
# A dictionary taht stores questions and answers
# Have a variable that tracks the score of the player
# Loop through the dictionary using the key values pairs
# Display each question to the user and allow them to answer
# Tell them if they are right or wrong
# Show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question2": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "What is the capital of Ghana?",
        "answer": "Accra"
    },
    "question4": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question5": {
        "question": "What is the capital of Togo?",
        "answer": "Lome"
    },
    "question6": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question7": {
        "question": "What is the capital of Mali?",
        "answer": "Bamako"
    },
    "question8": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question9": {
        "question": "What is the capital of South Africa?",
        "answer": "Cape Town"
    },
    "question10": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question11": {
        "question": "What is the capital of Zambia?",
        "answer": "Lusaka"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score+1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 11 questions correctly")
print("Your percentage is " + str(int(score/11 * 100)) + "%")
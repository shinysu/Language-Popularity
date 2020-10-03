'''
change the for loop that prints the answer options to use range(), so that the last value in the list(the correct answer)
is not printed
included lower() method to convert user input to lower case.
Remember, the correct answer that you give as last value in the answer list should also be in lower case
'''
quiz = {
    'What is the capital of India': ['Chennai', 'Delhi', 'Mumbai', 'delhi'],
    'What is the national bird of India': ['peacock', 'pigeon', 'parrot', 'peacock'],
    'What is the national animal of India': ['Lion', 'Cheetah', 'Tiger', 'tiger']
}

for questions, answers in quiz.items():
    print(questions)
    for i in range(len(answers)-1):
        print(answers[i])
    user_input = input().lower()
    if user_input == answers[-1]:
        print("Correct")
    else:
        print("Wrong answer")

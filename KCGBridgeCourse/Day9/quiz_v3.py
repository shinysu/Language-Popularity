'''
include the correct answer as the last value in the answer list
get the answer input from the user and check if it matches with the lat value in the answer list
'''
quiz = {
    'What is the capital of India': ['Chennai', 'Delhi', 'Mumbai', 'delhi'],
    'What is the national bird of India': ['peacock', 'pigeon', 'parrot', 'peacock'],
    'What is the national animal of India': ['Lion', 'Cheetah', 'Tiger', 'tiger']
}

for questions, answers in quiz.items():
    print(questions)
    for word in answers:
        print(word)
    user_input = input()
    if user_input == answers[-1]:
        print("Correct")
    else:
        print("Wrong answer")

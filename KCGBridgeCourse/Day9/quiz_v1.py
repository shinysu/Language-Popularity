'''
A quiz app where questions and answers are stored in a dictionary
The key for the dictionary is the question and the value is the list of options to be given to the user
'''
quiz = {
    'What is the capital of India': ['Chennai', 'Delhi', 'Mumbai'],
    'What is the national bird of India': ['peacock', 'pigeon', 'parrot'],
    'What is the national animal of India': ['Lion','Cheetah', 'Tiger']
}

for questions, answers in quiz.items():
    print(questions)
    print(answers)
'''
prints the questions and the options
'''
quiz = {
    'What is the capital of India': ['Chennai', 'Delhi', 'Mumbai'],
    'What is the national bird of India': ['peacock', 'pigeon', 'parrot'],
    'What is the national animal of India': ['Lion','Cheetah', 'Tiger']
}

for questions, answers in quiz.items():
    print(questions)
    for word in answers:
        print(word)
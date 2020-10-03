print("Hello! I'm an echobot. I can repeat whatever you say")
while True:
    inp = input().lower()
    if inp == 'hi' or inp == 'hello':
        print("hello")
    elif inp == 'bye' or inp == 'good bye':
        print('Good Bye')
        break
    else:
        print(inp)

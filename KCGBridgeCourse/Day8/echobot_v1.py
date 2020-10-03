print("Hello! I'm an echobot. I can repeat whatever you say")
while True:
    inp = input().lower()
    if inp == 'hi':
        print("hello")
    elif inp == 'bye':
        print('Good Bye')
        break
    else:
        print(inp)

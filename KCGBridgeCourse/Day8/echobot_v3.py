print("Hello! I'm an echobot. I can repeat whatever you say")
while True:
    inp = input().lower()
    if 'hi' in inp or 'hello' in inp:
        print("Hello There")
    elif 'name' in inp:
        print("My name is botty!")
    elif 'bye' in inp:
        print('Good Bye')
        break
    else:
        print(inp)

import json

filename = 'username.json'
name = ""

try: 
    with open(filename) as f:
        name = json.load(f)
        print("Welcome back, " + name + "!" )
except FileNotFoundError:
    name = input("Hello! What's your name?")
    with open(filename, 'w') as f:
        json.dump(name, f)
    print("We will remember you when you're back, " + name + "!")

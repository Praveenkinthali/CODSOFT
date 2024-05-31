import re
response_list = {
    "hello": "Hello!, How can i help you..",
    "hi": "Hi! ,How is your day..",
    "how can i call you": "you can just call me chat bot..",
    "how are you": "I'm just a bot, but I'm here to assist you!",
    "what is your name": "I'm a simple chatbot created to assist you.",
    "good|great" : "Glad to hear it...,is anyway i can assist you..",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, will you please don't mind,can you please rephrase it..?"
}

def response_need(input) :
    inp = input.lower()
    
    for pattern, response in response_list.items():
        if re.search(pattern, inp):
            return response
    
    return response_list["default"]

def chatbot():
    print("Chatbot: Hello!.. Type 'bye' to exit.")
    while True:
        inp = input("You: ")
        if inp.lower() == "bye":
            print("Chatbot: Goodbye! Enjoy your day!")
            break
        response_came = response_need(inp)
        print(f"Chatbot: {response_came}")

chatbot()
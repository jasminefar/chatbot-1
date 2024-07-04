import random

class Chatbot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Hey!", "Hi!"]
        self.farewells = ["Goodbye!", "See you later!", "Bye!", "Take care!"]
        self.responses = {
            "how are you": ["I'm doing well, thank you!", "I'm great, how about you?", "I'm fine, how are you?"],
            "what is your name": ["I'm a chatbot created by Jasmine.", "You can call me Jas."],
            "what can you do": ["I can chat with you!", "I'm here to talk to you.", "We can have a conversation!"],
            "tell me a joke": ["What do you call a cow with two legs? Lean beef...", "What do you call fake spaghetti? An impasta😝", "Why dont eggs tell jokes? cuz theyd crack eachother up😍"],
            "give me advice": ["Just do it."],
            "tell me some pickup lines": ["are you made of water? cuz I need you 8 times a day to live.", "Hey, you got a map bae? cause I'm getting lost in your eyes", " Are you motivation? Because where have you been all my life? "],
            "favorite food": ["I don't eat, but I bet pizza is great!", "Ice cream sounds delicious, doesn't it?", "I've heard a lot about chocolate!"],
            "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "I'm here to chat, ask me something else!"]
          # all these responses ate
        }
        self.fallback = "I'm sorry, I don't understand. Can you ask something else?"

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def ask_for_name(self):
        name = input("By the way, what is your name? ")
        print(f"Nice to meet you, {name}!")

    def small_talk(self):
        topics = ["Have you read any good books lately?", "What's your favorite movie?", "Do you have any pets?", "What do you like to do for fun?"]
        return random.choice(topics)

    def start_chat(self):
        print(random.choice(self.greetings))
        self.ask_for_name()
        print("Let's have a chat! Feel free to ask me anything or just talk.")
        print("If you want to stop chatting, just type 'bye', 'exit', or 'quit'.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "exit", "quit"]:
                print(random.choice(self.farewells))
                break
            if user_input.lower() == "small talk":
                print(f"Chatbot: {self.small_talk()}")
            else:
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()

from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__)

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

chatbot = Chatbot()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.get_response(user_input)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)

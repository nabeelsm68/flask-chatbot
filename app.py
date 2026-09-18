from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I'm ChatBot, your friendly assistant!"

    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Try asking something else."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot_response(user_input)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
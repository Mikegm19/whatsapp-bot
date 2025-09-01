from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# test route (open in browser)
@app.route('/')
def home():
    return "Your WhatsApp bot is live 🚀"

# Twilio webhook route
@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body("Hi there 👋, your bot is working!")
    elif 'exam' in incoming_msg:
        msg.body("Here’s your exam info 📘")
    else:
        msg.body("I didn’t understand that. Try saying 'hello' or 'exam'.")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

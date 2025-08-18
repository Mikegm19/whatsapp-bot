from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "exam" in incoming_msg:
        msg.body("📅 Next exams start on 12th September.")
    elif "result" in incoming_msg:
        msg.body("🎓 Sample result: John Doe - Math: 85, Science: 90, English: 88")
    elif "contact" in incoming_msg:
        msg.body("📞 School Contact: 080-1234-5678\n📧 Email: info@myschool.com")
    else:
        msg.body("Hi! Type 'exam', 'result', or 'contact' to get info.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "exam" in incoming_msg:
        msg.body("📅 Next exams start on 12th September.")
    elif "result" in incoming_msg:
        msg.body("🎓 Sample result: John Doe - Math: 85, Science: 90, English: 88")
    elif "contact" in incoming_msg:
        msg.body("📞 School Contact: 080-1234-5678\n📧 Email: info@myschool.com")
    else:
        msg.body("Hi! Type 'exam', 'result', or 'contact' to get info.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)


'''I have created this project using Twilio(A cloud communication service),Ngrok and flask.With the help of twilio we create a sandbox (for testing our bot).Twilio provides us a number and 
a phrase through which we can register our whatsapp number.Ngrok converts our local url to public url.Now all we have to do is to configure our sandbox through this url and then we are ready 
to use bot. We can deploy this on any application also such as Heroku so that our bot works even when our PC/laptop is closed.We can use Dialogbox and its agents to create a perfect conversational 
bot'''
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    

'''from flask import Flask, request
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
    #twilio whatsapp bot 

from flask import Flask,request,send_file
from twilio.twiml.messaging_response import MessagingResponse
import io
import datetime



appbot=Flask(__name__)
@appbot.route("/sms", methods=["get","post"])
def reply():
    with io.open("response.csv","a",encoding="utf-8")as f1:
        ur=request.form.get("Body")
        un=request.form.get("From")
        un=un.replace("whatsapp:","")
        dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
        data=un+","+ur+","+dt+"\n"
        print(un)
        f1.write(data)
        resp=MessagingResponse()
        msg=resp.message("you sent"+" "+ur+" "+"from"+" "+un+" "+"on"+" "+dt)
        return(str(resp))
        
    
    f1.close()
if (__name__=="__main__"):
 appbot.run()  '''
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime

apbot=Flask(__name__)
@apbot.route("/sms",methods=["get","post"])
def reply():
    msg_text=request.form.get("Body")
    sen_num=request.form.get("From")
    sen_num=sen_num.replace("whatsapp:","")
    msg=MessagingResponse()
    response=msg.message("you send " +msg_text +" from :"+sen_num)
    response1=msg.message("total technology logolaslaSLakslaSLAksas")
    response1.media("http://71d67779.ngrok.io/Users/roni/eclipse-workspace/watsappbot/w.jpg")
    return(str(msg))
    
    
    
    
    
    
if (__name__=="__main__"):
 apbot.run()
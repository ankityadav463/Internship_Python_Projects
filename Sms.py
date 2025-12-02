from twilio.rest import Client
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python! ",
    from_="+919522115147",   
    to="+918815172170"     
)

print("Message sent:", message.sid)
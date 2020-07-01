from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd201f574e9f63cbe8aca15e13011e383"
# Your Auth Token from twilio.com/console
auth_token  = "abc8011069944c8539d0ea4371323c8f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="6178200825", 
    from_="+12055095109",
    body="Hello from Python!")

print(message.sid)

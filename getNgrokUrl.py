import json
import os
from slackclient import SlackClient

slack_token = os.getenv("SLACK_API_TOKEN")
username = "@abeaumont"
if (slack_token is None):
    sys.exit(0)

sc = SlackClient(slack_token)

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:
    datajson = json.load(data_file)


msg = username+" ngrok URLs: "
for i in datajson['tunnels']:
    msg = msg + i['public_url'] + '\n'

sc.api_call(
    "chat.postMessage",
    channel="CA3QZ4B6Z",
    # user="U6DP58EH4",
    link_names=1,
    username="ngrok-url-bot",
    text=msg
)
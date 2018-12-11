# ngrok-python-url

Posting your ngrok rdp url to slack

## Installation steps

- Install requirements

  - You will need python 3 and pip
  - `pip install -r requirements.txt`

- Make sure you have ngrok and curl installed

  - Also authenticate ngrok if you have not done that aswell

- Retrive your slack api token

  - [link](https://api.slack.com/custom-integrations/legacy-tokens)

- Create a new Environment Variable

  - Called `SLACK_API_TOKEN` value of your copied token

- Create a basic task in windows

  - Point the task to the bat file included

- Change the username in the python script to your name in slack

- Run the task and everything should work!

import slack_sdk
import os
import requests
from dotenv import load_dotenv
from slack_bolt import App
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)
app1 = App(token=os.environ["SLACK_BOT_TOKEN"])
slack_event_adapter = SlackEventAdapter(os.environ["SIGNING_SECRET"], '/slack/events', app)

client = slack_sdk.WebClient(token=os.environ["SLACK_BOT_TOKEN"])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('file_shared')
def file_shared(payload):
    event = payload.get('event', {})
    resp = app1.client.files_info(token=os.environ["SLACK_BOT_TOKEN"], file=event['file_id'])
    file = resp['file']
    channel = file['channels'][0]
    fileshare = file['shares']['public'][channel]
    channel_name = fileshare[0]['channel_name']
    slack_token = os.environ['SLACK_BOT_TOKEN']
    hed = {'Authorization': 'Bearer ' + slack_token}
    res = requests.get(url=file['url_private'], headers=hed)
    res.raise_for_status()
    print(channel_name)
    with open('my_first_file', 'wb') as f:
        f.write(res.content)
    f.close
    name, extention = os.path.splitext(file['name'])
    print(extention)
    import shutil, os
    filename = [input("Enter file name:")]
    for files in filename:
        fileName, fileExtension = os.path.splitext(files)
        if fileExtension.endswith(".docx") or fileExtension.endswith(".pdf") or fileExtension.endswith(".doc"):

            # if fileExtension.endswith(".docx" or ".doc" or ".pdf"):
            print("This file is:", files)
            S3url = os.environ['S3_URL'] + channel_name + '/' + file['name']

            # print ('This file is:DOCX' and 'This file is PDF:' and 'This file is DOC:', files)
        elif fileExtension.endswith(".json"):
            print('This file is JSON:', files)
            S3url = os.environ['S3_JOBS_URL'] + channel_name + '/' + file['name']

        else:
            print('Format is not valid')
    '''if extention == ".docx" or ".doc" or ".pdf":
        S3url = os.environ['S3_URL'] + channel_name + '/' + file['name']
    elif extention == ".json":
        S3url = os.environ['S3_JOBS_URL'] + channel_name + '/' + file['name']'''

    print(S3url)
    headers = {'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
    resp = requests.put(S3url, data=open('my_first_file', 'rb'), headers=headers)
    print(resp)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

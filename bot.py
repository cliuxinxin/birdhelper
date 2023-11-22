import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})
    if data['event']['type'] == 'message' and 'subtype' not in data['event']:
        try:
            response = client.chat_postMessage(
                channel=data['event']['channel'],
                text="Hello World")
        except SlackApiError as e:
            print(f"Error posting message: {e}")
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)

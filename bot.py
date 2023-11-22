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
    print("Received a request")
    print(request.get_data(as_text=True))
    data = request.json

    # 方便调试
    print(data)

    # 响应Slack的URL验证
    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})

    # 检查是否存在 'event' 键
    if 'event' in data:
        event = data['event']

        # 处理app_mention事件
        if event.get('type') == 'app_mention':
            try:
                response = client.chat_postMessage(
                    channel=event['channel'],
                    text="Hello, I am your bot!")
            except SlackApiError as e:
                print(f"Error posting message: {e}")

    return '你好', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

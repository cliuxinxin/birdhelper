import os
from dotenv import load_dotenv
load_dotenv()
from slack_bolt import App

# 初始化您的应用
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# 定义事件处理函数
@app.event("app_mention")
def mention_handler(say):
    say("Hello World")

# 启动您的应用
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))



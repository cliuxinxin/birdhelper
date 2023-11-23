import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# 机器人的 Token
TOKEN = os.environ.get("TELE_BOT_TOKEN")

# 定义命令 /start 的处理函数
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('你好！我是回声机器人，我会重复你说的话。')

# 定义消息处理函数
def echo(update: Update, context: CallbackContext) -> None:
    received_text = update.message.text
    update.message.reply_text(received_text)

# 主函数，设置机器人的处理器
def main() -> None:
    updater = Updater(TOKEN)

    # 获取 dispatcher 来注册处理器
    dp = updater.dispatcher

    # 注册 /start 命令的处理器
    dp.add_handler(CommandHandler("start", start))

    # 注册消息处理器
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 开始轮询更新
    updater.start_polling()

    # 运行机器人，直到按下 Ctrl-C 或进程收到 SIGINT、SIGTERM 或 SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
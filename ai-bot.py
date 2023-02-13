import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes


# 定义回复的函数
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 获取用户发送的消息
    prompt = update.message.text

    # 设置 API 密钥
    openai.api_key = "你的openai秘钥"

    # 创建文本生成请求
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    # 向用户回复生成的文本
    await update.message.reply_text(response.choices[0].text)


# 创建 Telegram Bot 应用
app = ApplicationBuilder().token("tg机器人秘钥").build()

# 将回复函数添加到 Bot 应用中
app.add_handler(MessageHandler(None, hello))

# 启动 Bot
app.run_polling()

import os
import openai
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=os.getenv("tg_token"))
dp = Dispatcher(bot)

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("ai_token")


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
  await message.reply('Hello! I am SSE GPT chat bot. Ask me something')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
  await message.reply('What can I help You')


@dp.message_handler(commands=['stats'])
async def stats(message: types.Message):
  await message.reply('I am Alive')


@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  await message.reply(response.choices[0].text)


if __name__ == "__main__":
  executor.start_polling(dp)

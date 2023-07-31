import telebot # pip install pyTelegramBotAPI

from config import Security_1PSID, telegram_token # config.py is manually created file.

from bardapi import Bard #pip install bardapi

from colorama import Fore, Back, Style #pip install colorama

TOKEN = telegram_token

bot = telebot.TeleBot(TOKEN)
print(Fore.MAGENTA,'\nLogged In'.upper(),Style.RESET_ALL)
print(Fore.CYAN,'\nRUNNING...',Style.RESET_ALL)

@bot.message_handler()
def main(message):
    bard = Bard(Security_1PSID, timeout=60)
    response = bard.get_answer(message.text)['content']
    bot.reply_to(message, response)


# Polling loop to keep the bot running
bot.polling(none_stop=True, timeout=60)
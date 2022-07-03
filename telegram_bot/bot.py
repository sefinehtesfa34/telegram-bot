import os 
import telebot
API_KEY="5441321150:AAHugoKdKc3ibLL8pXJRB8uo_kONDNqSn9A"
bot=telebot.TeleBot(API_KEY)
@bot.message_handler(commands=["Hello"])
def greetings(message):
    bot.reply_to(message,"Welcome to PythonUPBot!")

def boost(message):
    if len(message.text)>5:
        return True 
    return False

@bot.message_handler(func=boost)
def send_message(message):
    bot.send_message(message.chat.id,"What is happening here?")

bot.polling()



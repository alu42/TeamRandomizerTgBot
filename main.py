from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import misc

tgtoken = misc.tgtoken #str(os.environ.get('tgtoken'))
updater = Updater(token=tgtoken) # Токен API к Telegram
dispatcher = updater.dispatcher


def textMessage(bot, update):
    newtext = update.message.text
    #print(newtext)
    if "тима" in newtext.lower() or "тимур" in newtext.lower():
        bot.send_message(chat_id=update.message.chat_id, text="Не пиши мне больше!")
    if "quit()" in newtext.lower():
        print("STOP COMMAND!")
        updater.stop()


# Обработка команд
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет. Под кем ходишь?')


def jpg(bot, update):
    answer = ''
    if answer == "чёт нету":
        bot.send_message(chat_id=update.message.chat_id, text=answer)
    else:
        bot.send_photo(chat_id=update.message.chat_id, photo=answer)


start_command_handler = CommandHandler('start', start)
jpg_command_handler = CommandHandler('jpg', jpg)

text_message_handler = MessageHandler(Filters.text, textMessage)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(jpg_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()

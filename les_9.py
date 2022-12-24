from telebot import TeleBot, types
TOKEN = '5644346942:AAHdonF5jp5F55D0KWf1ZBdOOfsyTwIay8s'
bot = TeleBot(TOKEN)
# @bot.massege_handler()
# def answer(msg: types.Message):
#     bot.send_message(chat_id = msg.from_user.id, text = 'Вы прислали: ' + msg.text)
 
 
# @bot.message_handler()
# def answer(msg: types.Message):
 
#     text = msg.text
 
#     if int(text) % 2 == 0:
#         bot.register_next_step_handler(msg, answer1)
#     else:
#         bot.register_next_step_handler(msg, answer2)
 
#     bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text)
 
 
# def answer1(msg):
#     bot.send_message(chat_id=msg.from_user.id, text='Вы ввели чётное число')
 
 
# def answer2(msg):
#     bot.send_message(chat_id=msg.from_user.id, text='Вы ввели нечётное число')
 
 
# bot.polling()


# from telebot import TeleBot, types
 
# TOKEN = ''
 
# bot = TeleBot(TOKEN)
 
 
@bot.message_handler()
def answer(msg: types.Message):
 
    text = msg.text
 
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')
 
 
def answer1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
 
 
def answer2(msg):
    a, b = map(int,  msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
 
 
bot.polling()


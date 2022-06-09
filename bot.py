import telebot


TOKEN = '5388942012:AAFitwXnb-7r1PJE5ciwYXvovvFZHPhLcc8'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')


def calc_of_medium_energy_level(power, deal_list):
    return power/sum(deal_list.values())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = '10.00'
    item2 = '20.00'
    user_markup.add(item1, item2)

    msg = bot.reply_to(message, f'Hello {message.from_user.first_name}, when should I track your time?', reply_markup=user_markup)
    bot.register_next_step_handler(msg, energy_max)


def energy_max(message):
    msg = bot.send_message(message.chat.id, 'if you have 100% energy in the morning what can you do. One case, then width')
    bot.register_next_step_handler(msg, energy_max_cases_width)


def energy_max_cases_width(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = '1'
    item2 = '2'
    item3 = '3'
    item4 = '4'
    item5 = '5'
    user_markup.add(item1, item2, item3, item4, item5)
    msg = bot.send_message(message.chat.id, 'How hard is that?', reply_markup=user_markup)
    bot.register_next_step_handler(msg, end)


def end(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = 'yes'
    item2 = 'no'
    user_markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, 'Should we end?', reply_markup=user_markup)
    bot.register_next_step_handler(msg, calc_power)


def calc_power(message):
    if message.text == 'yes':
        bot.send_message(message.chat.id, 'I am going ask you about power by schedule')
    if message.text == 'no':
        msg = bot.send_message(message.chat.id,
                               'one more case')
        bot.register_next_step_handler(msg, energy_max_cases_width)

def input_today_power(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = '10'
    item2 = '20'
    item3 = '40'
    item4 = '60'
    item5 = '80'
    item6 = '100'
    user_markup.add(item1, item2, item3, item4, item5, item6)
    msg = bot.send_message(message.chat.id, 'What is your energy level', reply_markup=user_markup)
    bot.register_next_step_handler(msg, end)


bot.infinity_polling()

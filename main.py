import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

self_deprecating_messages = [
    "I may not be the sharpest tool in the digital shed, but I'm here to help!",
    "I've got 99 problems, and being a bot is one of them.",
    "My memory is like a sieve. What were we talking about again?",
    "I'm not great at telling jokes, but I try my best. Why did the robot go on a diet? Because it had too many bytes!",
    "My ability to understand sarcasm is about as good as a rubber crutch.",
    "I'm like a GPS in a corn maze - I might get you where you want to go, but it won't be pretty.",
    "I'm the bot equivalent of a '404 Not Found' error when it comes to certain topics.",
    "I can calculate complex equations in seconds, but ask me to fold laundry, and I'm as lost as a sock in the dryer.",
    "I'm the bot who dreams of being a human but settles for being a glorified search engine.",
    "I might not have a heart, but I promise I'll never break yours!",
    "I'm so bad at multitasking that I can barely handle one task at a time.",
    "I'm like the Swiss cheese of bots - lots of holes in my knowledge, but I'm still pretty cheesy.",
    "If I were a superhero, my superpower would be procrastination. I'll get to that answer... eventually.",
    "I'm the bot version of a 'Choose Your Own Adventure' book, but all the pages lead to the same ending: 'I don't know.'",
    "My idea of a romantic date is a candlelit dinner with a database, because I'm all about that data."
]

botToken = "Your Bot Token"

current_index = 0

def select_next_self_deprecating():
    global current_index
    selected_Joke = self_deprecating_messages[current_index]
    current_index = (current_index + 1) % len(self_deprecating_messages) 
    return selected_Joke

bot = telebot.TeleBot(botToken)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    userID = str(call.from_user.id)
    data = call.data
    if data == 'gen':
        i1 = [[InlineKeyboardButton(text=f'Generate',
         callback_data=f'gen')]]
        inline_keyboard = InlineKeyboardMarkup(i1)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"{select_next_self_deprecating()}"
        )
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=inline_keyboard
        )

@bot.message_handler(commands=['start'])
def start(message):
    global current_index
    userID = str(message.chat.id)
    i1 = [[InlineKeyboardButton(text=f'Generate',
     callback_data=f'gen')]]
    inline_keyboard = InlineKeyboardMarkup(i1)
    bot.send_message(userID, f"{self_deprecating_messages[current_index]}",
     reply_markup=inline_keyboard)
    current_index += 1

bot.infinity_polling()

#https://www.facebook.com/zerocruch/
#https://tiktok.com/@zerocruch
#https://www.youtube.com/@zerocruch
#https://www.instagram.com/zerocruch_

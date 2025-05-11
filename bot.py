import telebot

API_TOKEN = '7873516365:AAEasMi70i00R922n6c0sUBK8S735Lw3xxQ'

bot = telebot.TeleBot(API_TOKEN)

CHANNELS = ['@nurrrikx', '@playlist_nurrrikx', '@chatnurrrikx']
SPECIAL_LINK = 'https://t.me/+gkEa4AjC_9g0ODQ6'

def is_subscribed(user_id):
    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                return False
        except:
            return False
    return True

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Сәлем! Ботты пайдалану үшін келесі каналдарға жазыл:\n\n"
    for channel in CHANNELS:
        text += f"{channel}\n"
    text += "\nЖазылған соң /check деп жаз."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['check'])
def check_subscription(message):
    user_id = message.from_user.id
    if is_subscribed(user_id):
        bot.send_message(user_id, f"Керемет! Міне сілтеме: {SPECIAL_LINK}")
    else:
        bot.send_message(user_id, "Сен барлық каналдарға жазылмадың. Қайта тексеріп көр.")

bot.polling()

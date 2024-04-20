import telebot
import random

bot = telebot.TeleBot('6860953287:AAHMkCgwxZqEIiRqgZfulbZXfV5XsT14ETs')

flag = False
secret = 0
@bot.message_handler(content_types=
	['text', 'document', 'audio'])

def get_text_messages(message):
	global flag
	global secret

	print(message)
	body = message.text
	if body == "Привет":
		bot.send_message(message.from_user.id,
		"Привет! </br> Напиши /help ля получения")
	elif body =="/help":
		bot.send_message(message.from_user.id,
			"Для запуска игры напиши /secret_number")
	elif body =="/secret_number":
		flag = "secret_number"
		secret = random.randrange(0, 100)
		bot.send_message(message.from_user.id,
			"Я загадал число от 0 до 100 ... попробуй угадать")
	elif flag =="secret_number":
		if int(body) < secret:
			bot.send_message(message.from_user.id,
				"Ваше число меньше")
		elif int(body) > secret:
			bot.send_message(message.from_user.id,
				"Ваше число больше")
		else:
			bot.send_message(message.from_user.id,
				"Вы выйграли")
	else:
		bot.send_message(message.from_user.id,
			"Для начала напишы /help")



bot.polling(none_stop=True, interval=0)
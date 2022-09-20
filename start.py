import vk_api
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from threading import Thread
import humanize

token = "vk1.a.Pg1ns9k6EK3UbgwpAlY4ye55WND7iY8o1YFuIJVG6Mb8gHDVNiumdx4cB10oW8F_dxPEe9Vf9Q8KQvoCkMDBsTvWdIoVnsoVKE3oYY_li43_BVYxYsNbEWHDEQu2-E9hyswVt6PNRaX2TsiX2g_I4khGhSnSHTk8Q-vwvKoQyQh0JTetiXJYu1lASd4vk1rM"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 214740674)
give = bh.get_api()

def main():
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.object.message['text'].lower())
			user_id = event.obj['message']['from_id']
			id = event.chat_id
			from methods import is_num, check_chat, elements_num, msg, reply_check, get_name, is_admin, kick, check_adm, shop, adm_inf, admin_menu, unban, ban, get_user_info, admin_take_off, admin_down, admin_up, give_tex, admin_cycle, check_reports, reply_mess, check_questions, start, get_my_bal, leave_admin_menu, chat_manage
			if event.from_user:
				if message == 'admin menu' or message == 'админ меню' or message == 'админ-меню' or message == 'admin-menu':
					admin_menu(message, user_id)
				elif message == 'разбан':
					unban(user_id)
				elif message == 'бан':
					ban(user_id)
				elif message == 'админ-инфо':
					adm_inf(user_id, user_id, 0)
				elif message == 'информация пользователя':
					get_user_info(user_id)
				elif message == 'выдать тех.поддержку':
					give_tex(user_id)
				elif message == 'повысить':
					admin_up(user_id)
				elif message == 'понизить':
					admin_down(user_id)
				elif message == 'снять':
					admin_take_off(user_id)
				elif message == 'администрация, которая в сети':
					admin_cycle(user_id)
				elif message == 'просмотр репортов':
					check_reports(user_id)
				elif message == 'просмотр вопросов':
					check_questions(user_id)
				elif message == 'начать':
					start(user_id)
				elif message == 'мой баланс':
					get_my_bal(user_id)
				elif message == 'выйти из админ-меню':
					leave_admin_menu(user_id)
				elif message == 'управление беседой':
					chat_manage(user_id)
			if event.from_chat:
				check_chat(id, user_id)
				if 'кик' in message or 'kick' in message or 'выгнать' in message or 'кикнуть' in message:
					user = reply_check(event)
					if user == False:
						if 'kick ' in message:
							user = message.replace('kick ', '')
							kick(id, user)
						elif 'кик ' in message:
							user = message.replace('кик ', '')
							kick(id, user)
						elif 'кикнуть ' in message:
							user = message.replace('кикнуть ', '')
							kick(id, user)
						elif 'выгнать ' in message:
							user = message.replace('выгнать ', '')
							kick(id, user)
						else:
							msg(id, 'Неверный формат. Используйте "кик [Пользователь через @]" или "кик", ответив на сообщение пользователя.')
					else:
						kick = kick(id, user)
						if kick == False:
							msg(id, 'Неверный формат. Используйте "кик [Пользователь через @]" или "кик", ответив на сообщение пользователя.')
				elif message == 'магазин':
					shop(id, user_id)
				elif message == 'admin-info':
					adm_inf(user_id, id, 1)
				elif 'жалоба ' in message:
					user = reply_check(event)
					if user == False:
						msg(id, "Чтобы пожаловаться на пользователя, ответьте на его сообщение с нарушением и через пробел опишите проблему.")
					else:
						a = reply_mess(event)
						user_mess = message.replace('жалоба ', '')
						report = str(user) + ', ' + str(a) + ' `' + str(user_mess) + ':' + str(user_id) + '\n'
						print(report)
						try:
							with open('reports.txt', 'a', encoding="utf-8") as f:
								f.write(report)
						finally:
							f.close()
							msg(id, 'Жалоба отправлена модерации.')
				elif message == 'chat_id':
					msg(id, id)
			        






import time
import requests
					
try:
    main()
except requests.exceptions.ReadTimeout:
    print("\n Переподключение к серверам ВК \n")
    time.sleep(3)
    main()
finally:
	main()
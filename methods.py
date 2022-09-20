import vk_api
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import humanize

token = "vk1.a.Pg1ns9k6EK3UbgwpAlY4ye55WND7iY8o1YFuIJVG6Mb8gHDVNiumdx4cB10oW8F_dxPEe9Vf9Q8KQvoCkMDBsTvWdIoVnsoVKE3oYY_li43_BVYxYsNbEWHDEQu2-E9hyswVt6PNRaX2TsiX2g_I4khGhSnSHTk8Q-vwvKoQyQh0JTetiXJYu1lASd4vk1rM"
bh = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(bh, 214740674)
give = bh.get_api()

def create_keyboard(message, user_id):
	keyboard = VkKeyboard(one_time=True)
 
	if message == 'admin menu' or message == 'админ меню' or message == 'adminmen' or message == 'админ-меню':
		adm = get_as(user_id)
		if adm == 1:
			keyboard.add_button('Просмотр вопросов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Просмотр репортов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_line()
			keyboard.add_button('Админ-инфо', color=VkKeyboardColor.SECONDARY)
			keyboard.add_button('Информация пользователя', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Администрация, которая в сети', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Выйти из админ-меню', color=VkKeyboardColor.NEGATIVE)
		elif adm == 2:
			keyboard.add_button('Просмотр вопросов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Просмотр репортов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_line()
			keyboard.add_button('Админ-инфо', color=VkKeyboardColor.SECONDARY)
			keyboard.add_button('Информация пользователя', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Администрация, которая в сети', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Бан', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Выйти из админ-меню', color=VkKeyboardColor.NEGATIVE)
		elif adm == 3:
			keyboard.add_button('Просмотр вопросов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Просмотр репортов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_line()
			keyboard.add_button('Админ-инфо', color=VkKeyboardColor.SECONDARY)
			keyboard.add_button('Информация пользователя', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Администрация, которая в сети', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Разбан', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Бан', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Выйти из админ-меню', color=VkKeyboardColor.NEGATIVE)
		elif adm == 4 or adm == 5:
			keyboard.add_button('Просмотр вопросов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Просмотр репортов', color=VkKeyboardColor.POSITIVE)
			keyboard.add_line()
			keyboard.add_button('Админ-инфо', color=VkKeyboardColor.SECONDARY)
			keyboard.add_button('Информация пользователя', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Администрация, которая в сети', color=VkKeyboardColor.SECONDARY)
			keyboard.add_line()
			keyboard.add_button('Разбан', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Бан', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Выдать Тех.Поддержку', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Снять', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Повысить', color=VkKeyboardColor.POSITIVE)
			keyboard.add_button('Понизить', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Выйти из админ-меню', color=VkKeyboardColor.NEGATIVE)
	if message == 'key1_reports':
		keyboard.add_button('Начать просмотр репортов', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Вернуться в админ-меню', color=VkKeyboardColor.NEGATIVE)
	if message == 'report_do':
		keyboard.add_button('Забанить', color=VkKeyboardColor.NEGATIVE)
		keyboard.add_button('Удалить репорт', color=VkKeyboardColor.NEGATIVE)
		keyboard.add_line()
		keyboard.add_button('Понизить фактор доверия', color=VkKeyboardColor.NEGATIVE)
	if message == 'key1_questions':
		keyboard.add_button('Начать просмотр вопросов', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Вернуться в админ-меню', color=VkKeyboardColor.NEGATIVE)
	if message == 'questions_do':
		keyboard.add_button('Ответить', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Пропустить', color=VkKeyboardColor.SECONDARY)
	if message == 'menu':
		keyboard.add_button('Мой баланс', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Управление беседой', color=VkKeyboardColor.POSITIVE)
		adm = get_as(user_id)
		if int(adm) > 1 or int(adm) == 1:
			keyboard.add_line()
			keyboard.add_button('Админ-Меню', color=VkKeyboardColor.NEGATIVE)
	if message == 'chat_manage':
		keyboard.add_button('Выдача статусов', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Забаненые пользователи', color=VkKeyboardColor.POSITIVE)
		keyboard.add_line()
		keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)
	if message == 'chat_status_manage':
		keyboard.add_button('Выдать Модератора', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Выдать Гл.Модератора', color=VkKeyboardColor.POSITIVE)
		keyboard.add_line()
		keyboard.add_button('Выдать Администратора', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Выдать Гл.Администратора', color=VkKeyboardColor.POSITIVE)
		keyboard.add_line()
		keyboard.add_button('Выдать Владельца', color=VkKeyboardColor.NEGATIVE)
		keyboard.add_button('Снять все права', color=VkKeyboardColor.NEGATIVE)
		keyboard.add_line()
		keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)
	keyboard = keyboard.get_keyboard()
	return keyboard

def is_num(str):
	try:
		float(str)
		return True
	except ValueError:
		return False

def elements_num(list):
	count = 0
	for element in list:
		count += 1
	return count

def msg(id, text):
	bh.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id': 0})
def send(id, text, keyboard):
	bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, 'keyboard' : keyboard})

def reply_check(event):
	msg_inf = event.obj['message']
	if 'reply_message' in msg_inf:
		reply_check = msg_inf['reply_message']['from_id']
		return reply_check
	else:
		return False

def reply_mess(event):
	msg_inf = event.obj['message']
	if 'reply_message' in msg_inf:
		text = msg_inf['reply_message']['text']
		return text

def get_balance(user):
	db = sqlite3.connect('chats.db')
	cur = db.cursor()
	sql = "select * from GLOBAL_DB where id = ?"
	cur.execute(sql, (user,))
	records = cur.fetchall()
	for record in records:
		cur.close()
		bal = record[1]
		return bal

def get_hide(user):
	db = sqlite3.connect('chats.db')
	cur = db.cursor()
	sql = "select * from GLOBAL_DB where id = ?"
	cur.execute(sql, (user,))
	records = cur.fetchall()
	for record in records:
		cur.close()
		bal = record[3]
		return bal

def get_factor(user):
	db = sqlite3.connect('chats.db')
	cur = db.cursor()
	sql = "select * from GLOBAL_DB where id = ?"
	cur.execute(sql, (user,))
	records = cur.fetchall()
	for record in records:
		cur.close()
		bal = record[5]
		return bal

def shop(id, user_id):
	bal = getbalance(user_id)
	msg(id, 'Добро пожаловать в магазин PRIMAT-MODER🛒\nТвой баланс: ' + str(bal) + ' Коинов💰\n\nindev...')

def get_name(uid: int) -> str:
	if int(uid) > 0:
		da = bh.method("users.get", {"user_ids": uid})
		dat = str(da)
		dat1 = dat.split("'first_name' : ")[0]
		data = dat1.replace("'", "")
		data_ = data.replace("'", "")
		d = data_.split(',')[1]
		data_f = d.replace(' first_name:', '')
		return data_f

def get_as(user_id):
	try:
		sqlite_connection = sqlite3.connect('chats.db')
		cursor = sqlite_connection.cursor()

		sql_select_query = """select * from GLOBAL_DB where id = ?"""
		cursor.execute(sql_select_query, (user_id,))
		records = cursor.fetchall()
		for record in records:
			cursor.close()
			admin = record[2]
			return admin
	except sqlite3.Error as error:
		a = 0
		a += 1
	finally:
		if (sqlite_connection):
			sqlite_connection.close()

def is_admin(id):
	info = bh.method('messages.getConversationMembers', {'peer_id' : 2000000000 + int(id)})
	information = info['items']
	inf = information[0]
	ifn = str(inf)
	if 'is_owner' in ifn:
		user = inf['member_id']
		return user

def kick(id, user_id):
	try:
		num_check = is_num(user_id)
		if num_check == True:
			bh.method('messages.removeChatUser', {'chat_id' : id, 'member_id' : user_id})
			msg(id, '[id' + str(user) + '|Участник] был исключён из беседы.')
			return True
		else:
			return False
	except vk_api.exceptions.ApiError:
		msg(id, 'Доступ запрещён. Невозможно исключить пользователя, возможно он является администратором или создателем беседы.')

def check_chat(chat_id, id):
	try:
		db = sqlite3.connect('chats.db')
		cursor = db.cursor()
		table = 'CHAT_' + str(chat_id)
		db.execute('''CREATE TABLE {table} (
			id BIGINT,
			nickname TEXT,
			admin_lvl INT,
			ban_state INT)'''.format(table=table))
		db.commit()

		check_adm(chat_id, id)

	except sqlite3.Error as error:
		check_adm(chat_id, id)
	finally:
		if (db):
			db.close()

def check_adm(id, user):
	is_adm = is_admin(id)
	table = 'CHAT_' + str(id)
	db = sqlite3.connect('chats.db')
	cursor = db.cursor()		
	db.commit()
	g = "INSERT INTO GLOBAL_DB VALUES (?, ?, ?, ?, ?, ?)"

	met = "SELECT * FROM " + table + " WHERE id = ?"
	cursor.execute(met, (is_adm,))
	db.commit()
	name = get_name(is_adm)
	if cursor.fetchone() is None:
		cursor.execute(f"INSERT INTO " + table + f" VALUES (?, ?, ?, ?)", (int(is_adm), name, 5, 0))
		db.commit()
		cursor.execute(g, (int(user), 0, 0, 0, 0, 50))

	met1 = "SELECT * FROM " + table + " WHERE id = ?"
	cursor.execute(met1, (user,))
	name1 = get_name(user)
	if cursor.fetchone() is None:
		cursor.execute(f"INSERT INTO " + table + f" VALUES (?, ?, ?, ?)", (int(user), name1, 0, 0))
		db.commit()
		cursor.execute(g, (int(user), 0, 0, 0, 50))
		db.commit()
		db.close()
	else:
		cursor.close()

def adm_inf(user_id, id, stat):
	if stat == 1:
		bal = get_balance(user_id)
		adm = get_as(user_id)
		hide = get_hide(user_id)
		if int(adm) > 1 or int(adm) == 1:
			if adm == 1:
				adm_stat = '[1] Тех.Поддержка'
			elif adm == 2:
				adm_stat = '[2] Модератор'
			elif adm == 3:
				adm_stat = '[3] Администратор'
			elif adm == 4:
				adm_stat = '[4] Тимлид Стаффа'
			elif adm == 5:
				adm_stat = '[5] Владелец'
			if hide == 0:
				hide_stat = 'Вы не скрываете свой статус.'
			elif hide == 1:
				hide_stat = 'Вы скрываете свой статус.'
			msg(id, '🛡Ты попал в админ-инфо🛡\n\n💸Твой баланс: ' + str(bal) + ' Коинов💰\n📍Твой статус: ' + adm_stat + '\n🧪' + hide_stat)
	else:
		bal = get_balance(user_id)
		adm = get_as(user_id)
		hide = get_hide(user_id)
		if int(adm) > 1 or int(adm) == 1:
			if adm == 1:
				adm_stat = '[1] Тех.Поддержка'
			elif adm == 2:
				adm_stat = '[2] Модератор'
			elif adm == 3:
				adm_stat = '[3] Администратор'
			elif adm == 4:
				adm_stat = '[4] Тимлид Стаффа'
			elif adm == 5:
				adm_stat = '[5] Владелец'
			if hide == 0:
				hide_stat = 'Вы не скрываете свой статус.'
			elif hide == 1:
				hide_stat = 'Вы скрываете свой статус.'
			send(user_id, '🛡Ты попал в админ-инфо🛡\n\n💸Твой баланс: ' + str(bal) + ' Коинов💰\n📍Твой статус: ' + adm_stat + '\n🧪' + hide_stat, create_keyboard('админ меню', user_id))

def admin_menu(message, user_id):
	name = get_name(user_id)
	adm = get_as(user_id)
	if int(adm) > 1 or int(adm) == 1:
		if adm == 1:
			status = '[1] Тех.Поддержка'
		elif adm == 2:
			status = '[2] Модератор'
		elif adm == 3:
			status = '[3] Администратор'
		elif adm == 4:
			status = '[4] Тимлид Стаффа'
		elif adm == 5:
			status = '[5] Владелец'
		send(user_id, '🛡Ты попал в админ-меню🛡\nВнизу есть кнопки, которые тебе доступны.\nКнопки зависят от твоего статуса.\nСейчас твой статус: ' + status, create_keyboard(message, user_id))

def is_ban(user_id):
	try:
		sqlite_connection = sqlite3.connect('chats.db')
		cursor = sqlite_connection.cursor()

		sql_select_query = """select * from GLOBAL_DB where id = ?"""
		cursor.execute(sql_select_query, (user_id,))
		records = cursor.fetchall()
		for record in records:
			cursor.close()
			ban_state = record[4]
			return ban_state
	except sqlite3.Error as error:
		print("[READ_DB] Ошибка при подключении к sqlite", error)
	finally:
		if (sqlite_connection):
			sqlite_connection.close()

def get_last_msg(id):
	info = bh.method('messages.getHistory', {'user_id' : id, 'count': 1})
	text = info['items']
	text = text[0]['text']
	return text

def unban_user(user_id, link):
	link = link.replace('https://vk.com/', '')
	if 'id' in link or '@id' in link:
		send(user_id, 'Разбаниваю пользователя ' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Разбаниваю пользователя ', '')
		userr = u_id.split("|")[0]
		user = userr.replace('[', '')
		if "id" in user:
			user = user.replace("id", "")
		ban_status = is_ban(user)
		if ban_status == 1:
			sqlite_connection = sqlite3.connect('chats.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE GLOBAL_DB SET ban_stat = ? WHERE id = ?""", (0, user))
			sqlite_connection.commit()
			cur.close()
			send(user_id, '✅[id' + str(user) + '|Пользователь] успешно разбанен.', create_keyboard('adminmen', int(user_id)))
		else:
			send(user_id, '❌[id' + str(user) + '|Пользователь] не имеет бана.', create_keyboard('adminmen', int(user_id)))
	else:
		send(user_id, 'Разбаниваю пользователя @' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Разбаниваю пользователя ', '')
		if "@" in u_id:
			userr = u_id.split("|")[0]
			user = userr.replace('[', '')
			if "id" in user:
				user = user.replace("id", "")
		ban_status = is_ban(user)
		if ban_status == 1:
			sqlite_connection = sqlite3.connect('chats.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE GLOBAL_DB SET ban_stat = ? WHERE id = ?""", (0, user))
			sqlite_connection.commit()
			cur.close()
			send(user_id, '✅[id' + str(user) + '|Пользователь] успешно разбанен.', create_keyboard('adminmen', int(user_id)))
		else:
			send(user_id, '❌[id' + str(user) + '|Пользователь] не имеет бана.', create_keyboard('adminmen', int(user_id)))
def ban_user(user_id, link):
	link = link.replace('https://vk.com/', '')
	if 'id' in link or '@id' in link:
		send(user_id, 'Баню пользователя ' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Баню пользователя ', '')
		userr = u_id.split("|")[0]
		user = userr.replace('[', '')
		if "id" in user:
			user = user.replace("id", "")
		ban_status = is_ban(user)
		if ban_status == 0:
			sqlite_connection = sqlite3.connect('chats.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE GLOBAL_DB SET ban_stat = ? WHERE id = ?""", (1, user))
			sqlite_connection.commit()
			cur.close()
			send(user_id, '✅[id' + str(user) + '|Пользователь] успешно забанен.', create_keyboard('adminmen', int(user_id)))
		else:
			send(user_id, '❌[id' + str(user) + '|Пользователь] уже забанен.', create_keyboard('adminmen', int(user_id)))
	else:
		send(user_id, 'Баню пользователя @' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Баню пользователя ', '')
		if "@" in u_id:
			userr = u_id.split("|")[0]
			user = userr.replace('[', '')
			if "id" in user:
				user = user.replace("id", "")
		ban_status = is_ban(user)
		if ban_status == 0:
			sqlite_connection = sqlite3.connect('chats.db')
			cur = sqlite_connection.cursor()

			cur.execute(f"""UPDATE GLOBAL_DB SET ban_stat = ? WHERE id = ?""", (1, user))
			sqlite_connection.commit()
			cur.close()
			send(user_id, '✅[id' + str(user) + '|Пользователь] успешно забанен.', create_keyboard('adminmen', int(user_id)))
		else:
			send(user_id, '❌[id' + str(user) + '|Пользователь] уже забанен.', create_keyboard('adminmen', int(user_id)))
def ban(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которого надо забанить.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					ban_user(user_id, link)
					break

def unban(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которого надо разбанить.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					unban_user(user_id, link)
					break

def user_info(user_id, link):
	link = link.replace('https://vk.com/', '')
	if 'id' in link or '@id' in link:
		send(user_id, 'Получаю информацию пользователя ' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Получаю информацию пользователя ', '')
		userr = u_id.split("|")[0]
		user = userr.replace('[', '')
		if "id" in user:
			user = user.replace("id", "")
		ban_status = is_ban(user)
		bal = get_balance(user)
		adm = get_as(user)
		hide = get_hide(user)
		if int(adm) > 1 or int(adm) == 1:
			if adm == 1:
				adm_stat = '[1] Тех.Поддержка'
			elif adm == 2:
				adm_stat = '[2] Модератор'
			elif adm == 3:
				adm_stat = '[3] Администратор'
			elif adm == 4:
				adm_stat = '[4] Тимлид Стаффа'
			elif adm == 5:
				adm_stat = '[5] Владелец'
			if hide == 0:
				hide_stat = 'Он не скрываете свой статус.'
			elif hide == 1:
				hide_stat = 'Он скрываете свой статус.'
			if ban_status == 1:
				ban = "📕Он забанен"
			elif ban_status == 0:
				ban = "📗Он не забанен"
			info = '💸Его баланс: ' + str(bal) + ' Коинов💰\n📍Его статус: ' + adm_stat + '\n🧪' + hide_stat + '\n' + ban
			send(user_id, "Информация [id" + str(user) + "|пользователя]:\n\n" + info, create_keyboard('adminmen', int(user_id)))
		else:
			if ban_status == 1:
				ban = "📕Он забанен"
			elif ban_status == 0:
				ban = "📗Он не забанен"
			info = '💸Его баланс: ' + str(bal) + ' Коинов💰\n📍Пользователь не является администратором\n' + ban
			send(user_id, "Информация [id" + str(user) + "|пользователя]:\n\n" + info, create_keyboard('adminmen', int(user_id)))
	else:
		send(user_id, 'Получаю информацию пользователя @' + str(link), None)
		uid = get_last_msg(user_id)
		u_id = uid.replace('Получаю информацию пользователя ', '')
		if "@" in u_id:
			userr = u_id.split("|")[0]
			user = userr.replace('[', '')
			if "id" in user:
				user = user.replace("id", "")
		ban_status = is_ban(user)
		bal = get_balance(user)
		adm = get_as(user)
		hide = get_hide(user)
		if int(adm) > 1 or int(adm) == 1:
			if adm == 1:
				adm_stat = '[1] Тех.Поддержка'
			elif adm == 2:
				adm_stat = '[2] Модератор'
			elif adm == 3:
				adm_stat = '[3] Администратор'
			elif adm == 4:
				adm_stat = '[4] Тимлид Стаффа'
			elif adm == 5:
				adm_stat = '[5] Владелец'
			if hide == 0:
				hide_stat = 'Он не скрываете свой статус.'
			elif hide == 1:
				hide_stat = 'Он скрываете свой статус.'
			if ban_status == 1:
				ban = "📕Он забанен"
			elif ban_status == 0:
				ban = "📗Он не забанен"
			info = '💸Его баланс: ' + str(bal) + ' Коинов💰\n📍Его статус: ' + adm_stat + '\n🧪' + hide_stat + '\n' + ban
			send(user_id, "Информация [id" + str(user) + "|пользователя]:\n\n" + info, create_keyboard('adminmen', int(user_id)))
		else:
			if ban_status == 1:
				ban = "📕Он забанен"
			elif ban_status == 0:
				ban = "📗Он не забанен"
			info = '💸Его баланс: ' + str(bal) + ' Коинов💰\n📍Пользователь не является администратором\n' + ban
			send(user_id, "Информация [id" + str(user) + "|пользователя]:\n\n" + info, create_keyboard('adminmen', int(user_id)))
		

def get_user_info(user_id):
	send(user_id, "Вставьте ссылку на пользователя, информацию которого нужно получить.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					user_info(user_id, link)
					break

def give_tex(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которому надо дать [1] Тех.Поддержку.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					link = link.replace('https://vk.com/', '')
					if 'id' in link or '@id' in link:
						send(user_id, 'Выдаю пользователю [1] Тех.Поддержку ' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Выдаю пользователю [1] Тех.Поддержку ', '')
						userr = u_id.split("|")[0]
						user = userr.replace('[', '')
						if "id" in user:
							user = user.replace("id", "")

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (1, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] был выдан статус [1] Тех.Поддержка', create_keyboard('adminmen', int(user_id)))
						break
					else:
						send(user_id, 'Выдаю пользователю [1] Тех.Поддержку @' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Выдаю пользователю [1] Тех.Поддержку ', '')
						if "@" in u_id:
							userr = u_id.split("|")[0]
							user = userr.replace('[', '')
							if "id" in user:
								user = user.replace("id", "")
						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (1, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] был выдан статус [1] Тех.Поддержка', create_keyboard('adminmen', int(user_id)))
						break
						

def admin_up(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которого нужно повысить.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					link = link.replace('https://vk.com/', '')
					if 'id' in link or '@id' in link:
						send(user_id, 'Повышаю пользователя ' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Повышаю пользователя ', '')
						userr = u_id.split("|")[0]
						user = userr.replace('[', '')
						if "id" in user:
							user = user.replace("id", "")

						old_adm = get_as(user)

						new_adm = int(old_adm) + 1

						if new_adm == 1:
							adm_stat = '[1] Тех.Поддержка'
						elif new_adm == 2:
							adm_stat = '[2] Модератор'
						elif new_adm == 3:
							adm_stat = '[3] Администратор'
						elif new_adm == 4:
							adm_stat = '[4] Тимлид Стаффа'
						elif new_adm == 5:
							adm_stat = '[5] Владелец'

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (new_adm, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] повышен до статуса ' + adm_stat, create_keyboard('adminmen', int(user_id)))
						break
					else:
						send(user_id, 'Повышаю пользователя @' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Повышаю пользователя ', '')
						if "@" in u_id:
							userr = u_id.split("|")[0]
							user = userr.replace('[', '')
							if "id" in user:
								user = user.replace("id", "")

						old_adm = get_as(user)

						new_adm = int(old_adm) + 1

						if new_adm == 1:
							adm_stat = '[1] Тех.Поддержка'
						elif new_adm == 2:
							adm_stat = '[2] Модератор'
						elif new_adm == 3:
							adm_stat = '[3] Администратор'
						elif new_adm == 4:
							adm_stat = '[4] Тимлид Стаффа'
						elif new_adm == 5:
							adm_stat = '[5] Владелец'

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (new_adm, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] повышен до статуса ' + adm_stat, create_keyboard('adminmen', int(user_id)))
						break
						

def admin_down(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которого нужно понизить.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					link = link.replace('https://vk.com/', '')
					if 'id' in link or '@id' in link:
						send(user_id, 'Понижаю пользователя ' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Понижаю пользователя ', '')
						userr = u_id.split("|")[0]
						user = userr.replace('[', '')
						if "id" in user:
							user = user.replace("id", "")

						old_adm = get_as(user)

						new_adm = int(old_adm) - 1

						if new_adm == 1:
							adm_stat = '[1] Тех.Поддержка'
						elif new_adm == 2:
							adm_stat = '[2] Модератор'
						elif new_adm == 3:
							adm_stat = '[3] Администратор'
						elif new_adm == 4:
							adm_stat = '[4] Тимлид Стаффа'
						elif new_adm == 5:
							adm_stat = '[5] Владелец'

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (new_adm, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] понижен до статуса ' + adm_stat, create_keyboard('adminmen', int(user_id)))
						break
					else:
						send(user_id, 'Понижаю пользователя @' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Понижаю пользователя ', '')
						if "@" in u_id:
							userr = u_id.split("|")[0]
							user = userr.replace('[', '')
							if "id" in user:
								user = user.replace("id", "")

						old_adm = get_as(user)

						new_adm = int(old_adm) - 1

						if new_adm == 1:
							adm_stat = '[1] Тех.Поддержка'
						elif new_adm == 2:
							adm_stat = '[2] Модератор'
						elif new_adm == 3:
							adm_stat = '[3] Администратор'
						elif new_adm == 4:
							adm_stat = '[4] Тимлид Стаффа'
						elif new_adm == 5:
							adm_stat = '[5] Владелец'

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (new_adm, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] понижен до статуса ' + adm_stat, create_keyboard('adminmen', int(user_id)))
						break

def admin_take_off(user_id):
	send(user_id, "Вставьте ссылку на пользователя, которого нужно снять.", None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			if event.from_user:
				link = str(event.object.message['text'].lower())
				if 'https://vk.com/' in link or '@' in link:
					link = link.replace('https://vk.com/', '')
					if 'id' in link or '@id' in link:
						send(user_id, 'Снимаю пользователя ' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Снимаю пользователя ', '')
						userr = u_id.split("|")[0]
						user = userr.replace('[', '')
						if "id" in user:
							user = user.replace("id", "")

						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (0, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] был снят.', create_keyboard('adminmen', int(user_id)))
						break
					else:
						send(user_id, 'Снимаю пользователя @' + str(link), None)
						uid = get_last_msg(user_id)
						u_id = uid.replace('Снимаю пользователя ', '')
						if "@" in u_id:
							userr = u_id.split("|")[0]
							user = userr.replace('[', '')
							if "id" in user:
								user = user.replace("id", "")
						sqlite_connection = sqlite3.connect('chats.db')
						cur = sqlite_connection.cursor()

						cur.execute(f"""UPDATE GLOBAL_DB SET admin_lvl = ? WHERE id = ?""", (0, user))
						sqlite_connection.commit()
						cur.close()
							
						send(user_id, "[id" + str(user) + '|Пользователю] был снят.', create_keyboard('adminmen', int(user_id)))
						break

def online_check(admin_id):
	is_on = bh.method('users.get', {'user_ids' : admin_id, 'fields' : 'online'})[0]
	is_online = is_on['online']
	if is_online == 1:
		return True
	else:
		return False
def checking(admin_id, admin_stat, admin_name):
	if admin_stat == 5:
		stat = '[5] Владелец'
	elif admin_stat == 4:
		stat = '[4] Тимлид Стаффа'
	elif admin_stat == 3:
		stat = '[3] Администратор'
	elif admin_stat == 2:
		stat = '[2] Модератор'
	elif admin_stat == 1:
		stat = '[1] Тех.Поддержка'
	return_ = '[id' + str(admin_id) + '|' + str(admin_name) + '] - ' + str(stat) + '\n'
	return return_

def admin_cycle(id):
	db = sqlite3.connect('chats.db', timeout=20)
	cursor = db.cursor()
	cursor.execute('SELECT id, admin_lvl FROM GLOBAL_DB ORDER BY admin_lvl DESC')
	one = cursor.fetchall()
	a = 0
	num = elements_num(one)
	full_list = ''
	while a < int(num):
		listt = one[int(a)]
		a += 1
		bb = str(listt)
		hh = bb.split(', ')[1]
		k = hh.replace(')', '')
		j = k.replace('(', '')
		if j != '0':
			idd = bb.split(', ')[0]
			ida = idd.replace('(', '')
			admin_id = ida.replace(')', '')
			admin_name = get_name(admin_id)
			admin_stat = get_as(admin_id)
			online = online_check(admin_id)
			if online == True:
				return_ = checking(admin_id, admin_stat, admin_name)
				if return_ == None:
					continue
				else:
					full_list = full_list + return_
	send(id, 'Администрация бота, которая сейчас в сети:\n\n' + full_list, create_keyboard('adminmen', int(id)))

def count_lines(txt):
	with open(txt) as f:
		line_count = 0
		for line in f:
			line_count += 1
		return line_count

def factor_method(user, from_report):
	factor = get_factor(user)
	factor_from = get_factor(from_report)
	if user == from_report:
		return False
	else:
		if factor < 10:
			return False

		else:
			sql = sqlite3.connect('chats.db', timeout=20)
			cur = sql.cursor()

			factor_new = int(factor) - 10

			from_report_factor = int(factor_from) + 10

			cur.execute("""UPDATE GLOBAL_DB SET factor = ? WHERE id = ?""", (factor_new, user))

			cur.execute("""UPDATE GLOBAL_DB SET factor = ? WHERE id = ?""", (from_report_factor, from_report))

			sql.commit()
			cur.close()

			return True

def second_rep(user_id, line):
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.object.message['text'].lower())
			if message == 'забанить':
				f = open('reports.txt', encoding="utf-8").read()
				res = f.replace(line,'')
				with open('reports.txt', 'w', encoding="utf-8") as f:
					f.write(res)
				user = '@id' + line.split(',')[0]
				ban_user(user_id, user)
				break
			elif message == 'удалить репорт':
				f = open('reports.txt', encoding="utf-8").read()
				res = f.replace(line,'')
				with open('reports.txt', 'w', encoding="utf-8") as f:
					f.write(res)
				send(user_id, "Репорт удалён.", None)
				break
			elif message == 'понизить фактор доверия':
				f = open('reports.txt', encoding="utf-8").read()
				res = f.replace(line,'')
				with open('reports.txt', 'w', encoding="utf-8") as f:
					f.write(res)
				user = line.split(',')[0]
				from_report = line.split(':')[1]
				fac = factor_method(user, from_report)
				if fac == True:
					send(user_id, "Фактор доверия пользователя понижен.", None)
				elif fac == False:
					send(user_id, "Фактор доверия не может быть понижен.\nБаню пользователя...", None)
					ban_user(user_id, user)
				else:
					send(user_id, 'error', None)
				break
			else:
				send(user_id, 'Используйте кнопки на клавиатуре!', create_keyboard('report_do', int(user_id)))
def check_reports(user_id):
	count = count_lines('reports.txt')
	send(user_id, 'Количество репортов в данный момент: ' + str(count), create_keyboard('key1_reports', int(user_id)))
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.object.message['text'].lower())
			if message == "вернуться в админ-меню":
				send(user_id, 'Возвращаю...', create_keyboard('adminmen', int(user_id)))
			elif message == 'начать просмотр репортов':
				b = 1
				a = 1
				while a > 0:
					if int(b) < int(count) or b == count:
						f = open('reports.txt', encoding="utf-8")
						for line in f:
							help = line.split('`')[0]
							user_rep = help.split(',')[0]
							user = '@id' + str(user_rep)
							text = help.split(',')[1]
							realsoon = line.split('`')[1]
							factorr = get_factor(user_rep)
							from_report = line.split(':')[1]
							realson = realsoon.split(':')[0]
							if int(factorr) > 70 and int(factorr) < 100:
								factor = 'Фактор доверия пользователя: 📗Отличный.'
							elif int(factorr) < 30 and int(factorr) > 0:
								factor = 'Фактор доверия пользователя: 📍Ужасный.'
							elif int(factorr) > 29 and int(factorr) < 71:
								factor = 'Фактор доверия пользователя: 🆕Нормальный.'
							else:
								factor = '⛔ОШИБКА: Не удалось определить фактор пользователя.'
							report = '✉На кого: ' + user + '\n🗒Текст репорта: ' + text + '\n💬Причина: ' + realson + '\n📊' + factor
							send(user_id, '📋Репорт от @id' + from_report + '\n' + report, create_keyboard('report_do', int(user_id)))
							second_rep(user_id, line)
						b += 1
					else:
						send(user_id, 'Репорты закончились(((', create_keyboard('key1_reports', int(user_id)))
						break

def second_ques(user_id, line):
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.object.message['text'].lower())
			if message == 'ответить':
				f = open('questions.txt', encoding="utf-8").read()
				user = f.split(',')[0]
				res = f.replace(line,'')
				with open('questions.txt', 'w', encoding="utf-8") as f:
					f.write(res)
				send(user_id, "Напишите сюда ответ пользователю", None)
				for event in longpoll.listen():
					if event.type == VkBotEventType.MESSAGE_NEW:
						answer = str(event.object.message['text'].lower())
						try:
							send(user, 'На ваш вопрос ответил администратор:\n' + str(answer), None)
							send(user_id, 'Вы отправили ответ пользователю.', create_keyboard('key1_questions', int(user_id)))
						except:
							send(user_id, 'Входящие сообщения пользователю заблокированы.', None)
						finally:
							break
				break
			elif message == 'пропустить':
				send(user_id, "Вопрос пропущен.", None)
				break
			else:
				send(user_id, 'Используйте кнопки на клавиатуре!', create_keyboard('questions_do', int(user_id)))

def check_questions(user_id):
	count = count_lines('questions.txt')
	send(user_id, 'Количество вопросов в данный момент: ' + str(count), create_keyboard('key1_questions', int(user_id)))
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			message = str(event.object.message['text'].lower())
			if message == "вернуться в админ-меню":
				send(user_id, 'Возвращаю...', create_keyboard('adminmen', int(user_id)))
			if message == 'начать просмотр вопросов':
				b = 1
				a = 1
				while a > 0:
					if int(b) < int(count) or b == count:
						f = open('questions.txt', encoding="utf-8")
						for line in f:
							user = '@id' + line.split(',')[0]
							text = line.split(',')[1]
							questions = 'От кого: ' + user + '\nТекст вопроса: ' + text
							send(user_id, 'Вопрос:\n' + questions, create_keyboard('questions_do', int(user_id)))
							second_ques(user_id, line)
						b += 1
					else:
						send(user_id, 'Вопросы закончились(((', create_keyboard('key1_questions', int(user_id)))
						break
			else:
				send(user_id, 'Используйте кнопки на клавиатуре!', create_keyboard('key1_questions', int(user_id)))


def start(user_id):
	send(user_id, 'Вы попали в меню бота.\nЧтобы управлять ботом используйте кнопки.', create_keyboard('menu', int(user_id)))

def get_all_banned_users(chat):
    sqlite_connection = sqlite3.connect('chats.db')
    
    cursor = sqlite_connection.cursor()

    sqlite_select_query = """SELECT * from {table}""".format(table=chat)
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    bans = 'Забаненые пользователи данной беседы:'
    for row in records:
        ban_state = row[3]
        if ban_state == 1:
            a = '\n' + '@id' + str(row[0])
            bans += a
    return bans

def leave_admin_menu(user_id):
	send(user_id, 'Вы вышли из админ-меню', create_keyboard('menu', int(user_id)))

def get_my_bal(user_id):
	balik = get_balance(user_id)
	send(user_id, "💸Твой баланс: " + str(balik) + ' Коинов💰', create_keyboard('menu', int(user_id)))

def chat_manage(user_id):
	send(user_id, 'Введите айди беседы, которую хотите настроить.\nАйди беседы можно узнать командой chat_id в беседе.', None)
	for event in longpoll.listen():
		if event.type == VkBotEventType.MESSAGE_NEW:
			try:
				mess = str(event.object.message['text'].lower())

				check = is_num(mess)
				if check == True:

					table = 'CHAT_' + str(mess)
					db = sqlite3.connect('chats.db')
					cursor = db.cursor()

					sql_select_query = """select * from {table} where id = ?""".format(table=table)
					cursor.execute(sql_select_query, (user_id,))
					records = cursor.fetchall()
					for record in records:

						cursor.close()
						admin = record[2]
						if int(admin) > 4 or int(admin) == 4:
							send(user_id, 'Доступ разрешён.\nВы перешли в режим управления беседой.\nИспользуйте кнопки для управления.', create_keyboard('chat_manage', int(user_id)))
							for event in longpoll.listen():
								if event.type == VkBotEventType.MESSAGE_NEW:
									message = str(event.object.message['text'].lower())
									if message == 'выдача статусов':
										send(user_id, 'Вы были перемещены в меню управления статусами в беседе.', create_keyboard('chat_status_manage', int(user_id)))
										for event in longpoll.listen():
											if event.type == VkBotEventType.MESSAGE_NEW:
												if event.from_user:

													sqlite_connection = sqlite3.connect('chats.db')
													cur = sqlite_connection.cursor()

													message = str(event.object.message['text'].lower())
													if message == 'выдать модератора':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link or '@' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Выдаю пользователю @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Выдаю пользователю ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (1, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'выдать гл.модератора':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link or '@' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Выдаю пользователю @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Выдаю пользователю ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (2, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'выдать администратора':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link or '@' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Выдаю пользователю @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Выдаю пользователю ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (3, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'выдать гл.администратора':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Выдаю пользователю @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Выдаю пользователю ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (4, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'выдать владельца':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link or '@' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Выдаю пользователю @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Выдаю пользователю ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (5, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'снять все права':
														send(user_id, 'Введите ссылку на пользователя.', None)
														for event in longpoll.listen():
															if event.type == VkBotEventType.MESSAGE_NEW:
																link = str(event.object.message['text'].lower())
																if 'https://vk.com/' in link or '@' in link:
																	link = link.replace('https://vk.com/', '')
																	send(user_id, 'Снимаю пользователя @' + str(link), None)
																	uid = get_last_msg(user_id)
																	u_id = uid.replace('Снимаю пользователя ', '')
																	userr = u_id.split("|")[0]
																	user = userr.replace('[', '')
																	if "id" in user:
																		user = user.replace("id", "")

																	cur.execute("""UPDATE {table} SET admin_lvl = ? WHERE id = ?""".format(table=table), (0, user))
																	sqlite_connection.commit()
																	send(user_id, 'Успех.', create_keyboard('chat_manage', int(user_id)))
																	break
													elif message == 'вернуться':
														send(user_id, 'Возвращаю.', create_keyboard('chat_manage', int(user_id)))
														break
													else:
														send(user_id, 'Используйте кнопки.', create_keyboard('chat_manage', int(user_id)))
														break
											break


									elif message == 'забаненые пользователи':
										bans_users = get_all_banned_users(table)
										send(user_id, bans_users, create_keyboard('chat_manage', int(user_id)))
									elif message == 'вернуться':
										send(user_id, 'Вы были возвращены в меню.', create_keyboard('menu', int(user_id))) 
									else:
										send(user_id, 'Используйте кнопки на клавиатуре.', create_keyboard('chat_manage', int(user_id)))
									break
						else:
							send(user_id, 'У вас нету прав управлять данной беседой.', create_keyboard('menu', int(user_id))) 
							break
						break
			except sqlite3.OperationalError:
				send(user_id, 'Беседы не существует.', create_keyboard('menu', int(user_id)))
				break
							
		break
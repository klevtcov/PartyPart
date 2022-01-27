import telebot
import partypart
import exceptions
from config import token


def telegram_bot(token):
    bot = telebot.TeleBot(token)


# Выводит приветственное сообщение
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Добро пожаловать в PartyPart\n\n"
                                          "Получить подробную справку о работе бота /info\n"
                                        #   "Посмотреть траты участника – Имя юзера\n"
                                        #   "Удалить запись о расходах /del\n"
                                          " Для добавления трат внесите данные в формате – Сумма Имя.\nНапример – 500 Сергей)\n"
                                          "Посмотреть итоги /total\n"
                                          "Вызвать справку /help или /start\n"
                                          "Удалить все записи о мероприятии /restart")


# Выводит справку о предназначении бота
    @bot.message_handler(commands=['info'])
    def info_message(message):
        bot.send_message(message.chat.id, "PatryPart – бот для учета расходов на мероприятие.\n\n"
                                          "Предположим, вы с друзьями решили устроить вечеринку:\n"
                                          "– Андрей купил вино за 1050 рублей и мандарины за 240\n"
                                          "– Пётр купил сыр за 500 и виноград за 370\n"
                                          "– Анна заказала суши за 1450\n"
                                          "– Вероника выбрала пиццу за 560\n"
                                          "– Сергей опаздывал на мероприятие и не успел купить ничего\n"
                                          "Вы вносите все эти траты в бота и он рассчитывает кому надо докинуть денег, а кому забрать из общего банка.")

# Выыод статистики
    @bot.message_handler(commands=['total'])
    def total_message(message):
        answer_message = partypart.total(message.chat.id)
        print(answer_message)
        bot.send_message(message.chat.id, answer_message)


    @bot.message_handler()
    def add_expense(message):
        # try:
        expense = partypart.add_expense(message.text, message.chat.id)
        # except exceptions.NotCorrectMessage(message.text, message.chat.id) as e:
        #     print(e, 'server.py')
        #     bot.send_message(message.chat.id, str(e))
        #     return
        answer_message = (
            f"Добавлены траты от {expense.user_name} на сумму {expense.amount}.\n\n"
            f"Посмотреть текущие итоги – /total")    
        bot.send_message(message.chat.id, answer_message)


    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
import requests
# from models.models import SportDB, LeagueDB, TeamsDB, Match_statusDB, MatchesDB

from extensions import extensions

# db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

# socketio = extensions.socketio
def telegram_bot_sendtext(bot_message, bot_token, bot_chatID):
    bot_token = bot_token
    bot_chatID = bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

@home.route('/')
def test():
    url = "https://api.telegram.org/bot5762791939:AAGJvJaY7FrUNpZ5OaZT9NtAmnVPhj2LgqU/getUpdates"
    chats_data = requests.get(url)
    chats_data_json = chats_data.json()
    list_of_updates = chats_data_json['result']
    chat_id = 0
    first_name = ""
    for update in list_of_updates:
        chat_id = update['message']['chat']['id']
        first_name = update['message']['chat']['first_name']

    # print(f"{first_name}: {chat_id}")
    bot_message = 'хуй'
    bot_token = '5762791939:AAGJvJaY7FrUNpZ5OaZT9NtAmnVPhj2LgqU'
    bot_chatID = chat_id
    send_message_json = telegram_bot_sendtext(bot_message, bot_token, bot_chatID)
    print(send_message_json)

    return render_template("test.html")

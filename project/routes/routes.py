from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
# from models.models import SportDB, LeagueDB, TeamsDB, Match_statusDB, MatchesDB
import requests
from extensions import extensions
import json

# db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

# socketio = extensions.socketio
amount = 0



@home.route('/')
def test():
    with open('currency_dict.json', 'r') as openfile:
        # Reading from json file
        currency_dict = json.load(openfile)

    with open('currency_dict_2.json', 'r') as openfile:
        # Reading from json file
        currency_dict_2 = json.load(openfile)

    # print(currency_dict)
    with open('saved_data.json', 'r') as openfile:
        # Reading from json file
        saved_data = json.load(openfile)

    # Обрабатываем список получателей сообщений
    TOKEN = "5762791939:AAGJvJaY7FrUNpZ5OaZT9NtAmnVPhj2LgqU"
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    bot_updates = requests.get(url).json()
    bot_updates_results = bot_updates['result']

    chat_data_dict = {}
    for bot_updates_result in bot_updates_results:
        if 'message' in list(bot_updates_result.keys()):
            temp_dict = {}
            chat_id = bot_updates_result['message']['from']['id']
            try:
                first_name = bot_updates_result['message']['from']['first_name']
                temp_dict['first_name'] = first_name
            except:
                pass
            try:
                username = bot_updates_result['message']['from']['username']
                temp_dict['username'] = username
            except:
                pass
            chat_data_dict[chat_id] = temp_dict

    with open("chats_data.json", "w", encoding='utf-8') as jsonFile:
        json.dump(chat_data_dict, jsonFile, ensure_ascii=False)

    with open('chats_data.json', 'r') as openfile:
        # Reading from json file
        chats_data = json.load(openfile)

    chat_data_dict = {}
    for chat_id, chat_data_value in chats_data.items():
        temp_dict = {}
        chat_id = int(chat_id)
        temp_dict['first_name'] = chat_data_value['first_name']
        temp_dict['username'] = chat_data_value['username']
        chat_data_dict[chat_id] = temp_dict


    return render_template("test.html", currency_dict_2=currency_dict_2, currency_dict=currency_dict, saved_data=saved_data, chat_data_dict = chats_data)


@home.route('/send_telegram_message', methods=["POST", "GET"])
def send_telegram_message():
    if request.method == 'POST':
        TOKEN = "5762791939:AAGJvJaY7FrUNpZ5OaZT9NtAmnVPhj2LgqU"
        telegram_chat_id = int(request.form.get('telegram_receiver'))

        # получаем данные о пересчете курсов
        with open('saved_data.json', 'r') as openfile:
            # Reading from json file
            saved_data = json.load(openfile)
            money_qty = saved_data["money_qty"]
            currency_from = saved_data["currency_from"]
            currency_to = saved_data["currency_to"]
            result = saved_data["result"]

        message = f"{money_qty} {currency_from} = {result} {currency_to}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={telegram_chat_id}&text={message}"
        # print(requests.get(url).json()) # this sends the message
        print("сообщение в телегу: ", requests.get(url))

        return redirect(url_for('home.test'))

@home.route('/convert_currency', methods=["POST", "GET"])
def convert_currency():
    if request.method == 'POST':
        saved_data_dict = {}
        money_requested_qty = float(request.form.get('money_requested_qty'))
        currency_from_id = request.form.get('currency_from')
        currency_to_id = request.form.get('currency_to')
        saved_data_dict['money_qty'] = money_requested_qty
        saved_data_dict['currency_from_id'] = currency_from_id
        saved_data_dict['currency_to_id'] = currency_to_id

        # читаем список валют
        with open('currency_dict_2.json', 'r') as openfile:
            # Reading from json file
            currency_dict_2 = json.load(openfile)
        currency_from_data_dict = currency_dict_2[currency_from_id]
        currency_from = ""
        for key, value in currency_from_data_dict.items():
            currency_from = value
        saved_data_dict['currency_from'] = currency_from

        currency_to_data_dict = currency_dict_2[currency_to_id]
        currency_to = ""
        for key, value in currency_to_data_dict.items():
            currency_to = value
        saved_data_dict['currency_to'] = currency_to


        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={money_requested_qty}"
        payload = {}
        headers = {
            "apikey": "uBkOvOx3IUayHeUSd4fcDMjsXQnvh6Or"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # status_code = response.status_code
        result = response.text
        result_json = response.json()
        currency_from = result_json['query']['from']
        currency_to = result_json['query']['to']
        amount = result_json['query']['amount']
        culc_result = result_json['result']
        saved_data_dict['amount'] = amount
        saved_data_dict['currency_from'] = currency_from
        saved_data_dict['currency_to'] = currency_to
        saved_data_dict['result'] = round(float(culc_result), 2)

        with open("saved_data.json", "w") as jsonFile:
            json.dump(saved_data_dict, jsonFile)

        return redirect(url_for('home.test'))


@home.route('/currency')
def currency():

    url = "https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=RUB&amount=100"


    payload = {}
    headers = {
        "apikey": "uBkOvOx3IUayHeUSd4fcDMjsXQnvh6Or"
    }

    # response = requests.request("GET", url, headers=headers, data=payload)

    # status_code = response.status_code
    # result = response.text
    # print(result)
    return render_template("test.html")
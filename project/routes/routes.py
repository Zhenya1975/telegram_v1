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
        money_qty = saved_data["money_qty"]
        currency_from = saved_data["currency_from"]
        currency_to = saved_data["currency_to"]
    return render_template("test.html", currency_dict=currency_dict, currency_dict_2=currency_dict_2, money_qty=money_qty, currency_from=currency_from, currency_to=currency_to)


@home.route('/convert_currency', methods=["POST", "GET"])
def convert_currency():
    if request.method == 'POST':
        money_requested_qty = float(request.form.get('money_requested_qty'))
        currency_from = request.form.get('currency_from')
        # print(currency_from)
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
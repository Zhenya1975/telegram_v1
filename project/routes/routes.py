from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
# from models.models import SportDB, LeagueDB, TeamsDB, Match_statusDB, MatchesDB

from extensions import extensions

# db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

# socketio = extensions.socketio

@home.route('/')
def test():
    return render_template("test.html")

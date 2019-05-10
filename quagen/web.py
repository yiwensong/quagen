import uuid

from flask import Blueprint
from flask import json
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from quagen.game import Game
from quagen import queries

bp = Blueprint('web', __name__)

@bp.route('/')
def index():
    game = Game()
    game.start()
    queries.insert_game(game)

    return redirect(url_for('web.game_view', game_id = game.game_id)) 

@bp.route('/game/<string:game_id>', methods = ['GET'])
def game_view(game_id):
    if 'player_id' not in session.keys():
        session['player_id'] = uuid.uuid4().hex

    game = queries.get_game(game_id).as_dict()  
    return render_template('game.html'
                         , game=game)



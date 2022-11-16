from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.Game import Game
import json

with open("character_class_configs.json") as f:
    reference_class_dict = json.load(f)

# print(reference_class_dict)

#### START ####
@app.route('/')
def display():
    return render_template('Dashboard.html')

@app.route('/game/new')
def gameNew():
    return render_template('charCreate.html')

@app.route('/character/create', methods=['POST'])
def characterCreate():
    

    print('game created')
    newGame = Game(reference_class_dict)
    
    print('character created')
    # char_type = request.form['archetype']
    # char_name = request.form["name"]
    # player1 = newGame.generateCharacter(reference_class_dict, char_type, char_name )
    
    data = {
        'archetype1': request.form['archetype1'],
        'archetype2': request.form['archetype2'],
        'name1': request.form['name1'],
        'name2': request.form['name2']
    }
    # print(reference_class_dict)
    # print(data)
    newGame.generateCharacter(data['archetype1'], data['name1'])
    newGame.generateCharacter(data['archetype2'], data['name2'])
    # player1 = newGame.characters[data['name']]
    # print(player1.name)
    # # print(player1.)
    return render_template('start.html', game = newGame)


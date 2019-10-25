from flask import Flask, render_template, request, session, redirect
from Player import Player
from Universe import Universe
from Game import Game
import json

app = Flask(__name__)
player = None
universe = None
game = None

@app.route('/')
def title_screen():
    global player
    player = None
    return render_template('TitleScreen.html')


@app.route('/config')
def config():
    global game
    difficulty = game.getDifficulty()
    print(difficulty)
    skillpts = 0
    if difficulty == 1:
        skillpts = 16
    elif difficulty == 2:
        skillpts = 12
    else:
        skillpts = 8
    return render_template("Config.html", skillpts=skillpts)


@app.route('/diff')
def diff():
    return render_template("Difficulty.html")

@app.route('/playerdata')
def playerdata():
    global player
    player_data = [player.getSailor()]
    return render_template("PlayerData.html", player_data=map(json.dumps, player_data))


@app.route('/DifficultyReceiver', methods=['POST'])
def difficultyparse():
    data = request.get_json()
    global game
    game = Game(data['difficulty'], ['China', 'India', 'Denmark', 'Great Britain',
                                          'Egypt', 'Somalia', 'Persia', 'Java',
                                          'Byzantium', 'Arabia'])
    global player
    player = Player(data['name'])
    skillpts = 0
    return None

@app.route('/SkillReceiver', methods=['POST'])
def skillparse():
    print(request)
    data = request.get_json()
    print(data)
    skillpts = 0
    global game
    if game.getDifficulty() == 1:
        skillpts = 16
    elif game.getDifficulty() == 2:
        skillpts = 12
    else:
        skillpts = 8

@app.route('/China')
def china():
    region_info = [Universe.getInstance().regions[0].getX(),
                   Universe.getInstance().regions[0].getY(),
                   Universe.getInstance().regions[0].getTechLevel()]
    return render_template("China.html", region_info=region_info)

@app.route('/India')
def india():
    region_info = [Universe.getInstance().regions[1].getX(),
                   Universe.getInstance().regions[1].getY(),
                   Universe.getInstance().regions[1].getTechLevel()]
    return render_template("India.html", region_info=region_info)

@app.route('/Denmark')
def denmark():
    region_info = [Universe.getInstance().regions[2].getX(),
                   Universe.getInstance().regions[2].getY(),
                   Universe.getInstance().regions[2].getTechLevel()]
    return render_template("Denmark.html", region_info=region_info)

@app.route('/Britain')
def britain():
    region_info = [Universe.getInstance().regions[3].getX(),
                   Universe.getInstance().regions[3].getY(),
                   Universe.getInstance().regions[3].getTechLevel()]
    return render_template("Britain.html", region_info=region_info)

@app.route('/Egypt')
def egypt():
    region_info = [Universe.getInstance().regions[4].getX(),
                   Universe.getInstance().regions[4].getY(),
                   Universe.getInstance().regions[4].getTechLevel()]
    return render_template("Egypt.html", region_info=region_info)

@app.route('/Somalia')
def somalia():
    region_info = [Universe.getInstance().regions[5].getX(),
                   Universe.getInstance().regions[5].getY(),
                   Universe.getInstance().regions[5].getTechLevel()]
    return render_template("Somalia.html", region_info=region_info)

@app.route('/Persia')
def persia():
    region_info = [Universe.getInstance().regions[6].getX(),
                   Universe.getInstance().regions[6].getY(),
                   Universe.getInstance().regions[6].getTechLevel()]
    return render_template("Persia.html", region_info=region_info)

@app.route('/Java')
def java():
    region_info = [Universe.getInstance().regions[7].getX(),
                   Universe.getInstance().regions[7].getY(),
                   Universe.getInstance().regions[7].getTechLevel()]
    return render_template("Java.html", region_info=region_info)

@app.route('/Byzantium')
def byzantium():
    region_info = [Universe.getInstance().regions[8].getX(),
                   Universe.getInstance().regions[8].getY(),
                   Universe.getInstance().regions[8].getTechLevel()]
    return render_template("Byzantium.html", region_info=region_info)

@app.route('/Arabia')
def arabia():
    region_info = [Universe.getInstance().regions[9].getX(),
                   Universe.getInstance().regions[9].getY(),
                   Universe.getInstance().regions[9].getTechLevel()]
    return render_template("Arabia.html", region_info=region_info)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

from flask import Flask, render_template, request, session, redirect, url_for
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
    Universe.__instance = None
    return render_template('TitleScreen.html')


@app.route('/diff')
def diff():
    return render_template("Difficulty.html")


@app.route('/DifficultyReceiver', methods=['POST'])
def difficultyparse():
    data = request.get_json()
    global game
    game = Game(data['difficulty'], ['China', 'India', 'Denmark', 'Great Britain',
                                          'Egypt', 'Somalia', 'Persia', 'Java',
                                          'Byzantium', 'Arabia'])
    global player
    player = Player(data['name'])
    return None


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


@app.route('/playerdata')
def playerdata():
    skillpts = 0
    global game
    global player
    game.startGame()
    if game.getDifficulty() == 1:
        skillpts = 16
        player.credits = 1000
    elif game.getDifficulty() == 2:
        skillpts = 12
        player.credits = 500
    else:
        skillpts = 8
        player.credits = 250
    if player.sailor + player.barterer + player.craftsman + player.cannoneer > skillpts:
        player.sailor = 0
        player.barterer = 0
        player.craftsman = 0
        player.cannoneer = 0
        return render_template("Failure.html")
    player_data = [player.name, player.credits, player.region.getName(), player.sailor, player.cannoneer, player.barterer, player.craftsman]
    return render_template("PlayerData.html", player_data=player_data)


@app.route('/SkillReceiver', methods=['POST'])
def skillparse():
    print(request)
    data = request.get_json()
    print(data)
    global player
    player.sailor = int(data['SailorPoints'])
    player.barterer = int(data['BartererPoints'])
    player.craftsman = int(data['CraftsmanPoints'])
    player.cannoneer = int(data['CannoneerPoints'])

@app.route('/China')
def china():
    global player
    region_info = [Universe.getInstance().regions[0].getX(),
                   Universe.getInstance().regions[0].getY(),
                   Universe.getInstance().regions[0].getTechLevel()]
    fuel_cost = Universe.getInstance().regions[0].get_fuel_cost(player.region.getX(), player.region.getY())
    if (fuel_cost <= player.ship.fuel):
        player.ship.fuel = player.ship.fuel - fuel_cost
        player.region = Universe.getInstance().regions[0]
        region_info.append(player.ship.fuel)
        return render_template("Regions/China.html", region_info=region_info)
    else:
        return redirect(url_for(player.region.getName().lower()))

@app.route('/India')
def india():
    region_info = [Universe.getInstance().regions[1].getX(),
                   Universe.getInstance().regions[1].getY(),
                   Universe.getInstance().regions[1].getTechLevel()]
    return render_template("Regions/India.html", region_info=region_info)

@app.route('/Denmark')
def denmark():
    region_info = [Universe.getInstance().regions[2].getX(),
                   Universe.getInstance().regions[2].getY(),
                   Universe.getInstance().regions[2].getTechLevel()]
    return render_template("Regions/Denmark.html", region_info=region_info)

@app.route('/Britain')
def britain():
    region_info = [Universe.getInstance().regions[3].getX(),
                   Universe.getInstance().regions[3].getY(),
                   Universe.getInstance().regions[3].getTechLevel()]
    return render_template("Regions/GreatBritain.html", region_info=region_info)

@app.route('/Egypt')
def egypt():
    region_info = [Universe.getInstance().regions[4].getX(),
                   Universe.getInstance().regions[4].getY(),
                   Universe.getInstance().regions[4].getTechLevel()]
    return render_template("Regions/Egypt.html", region_info=region_info)

@app.route('/Somalia')
def somalia():
    region_info = [Universe.getInstance().regions[5].getX(),
                   Universe.getInstance().regions[5].getY(),
                   Universe.getInstance().regions[5].getTechLevel()]
    return render_template("Regions/Somalia.html", region_info=region_info)

@app.route('/Persia')
def persia():
    region_info = [Universe.getInstance().regions[6].getX(),
                   Universe.getInstance().regions[6].getY(),
                   Universe.getInstance().regions[6].getTechLevel()]
    return render_template("Regions/Persia.html", region_info=region_info)

@app.route('/Java')
def java():
    region_info = [Universe.getInstance().regions[7].getX(),
                   Universe.getInstance().regions[7].getY(),
                   Universe.getInstance().regions[7].getTechLevel()]
    return render_template("Regions/Java.html", region_info=region_info)

@app.route('/Byzantium')
def byzantium():
    region_info = [Universe.getInstance().regions[8].getX(),
                   Universe.getInstance().regions[8].getY(),
                   Universe.getInstance().regions[8].getTechLevel()]
    return render_template("Regions/Byzantium.html", region_info=region_info)

@app.route('/Arabia')
def arabia():
    region_info = [Universe.getInstance().regions[9].getX(),
                   Universe.getInstance().regions[9].getY(),
                   Universe.getInstance().regions[9].getTechLevel()]
    return render_template("Regions/Arabia.html", region_info=region_info)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

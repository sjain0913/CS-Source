from flask import Flask, flash, render_template, request, session, redirect, url_for
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
    game = Game(data['difficulty'], ['China', 'India', 'Denmark', 'Britain',
                                          'Egypt', 'Somalia', 'Persia', 'Java',
                                          'Byzantium', 'Arabia'])
    global player
    player = Player(data['name'])
    return None


@app.route('/config')
def config():
    global game
    difficulty = game.getDifficulty()
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
    data = request.get_json()
    global player
    player.sailor = int(data['SailorPoints'])
    player.barterer = int(data['BartererPoints'])
    player.craftsman = int(data['CraftsmanPoints'])
    player.cannoneer = int(data['CannoneerPoints'])

@app.route('/trader')
def trader():
    return render_template("NPCs/Trader.html")

@app.route('/TraderReceiver', methods=['POST'])
def traderparse():
    data = request.get_json()

@app.route('/pirate')
def pirate():
    return render_template("NPCs/Pirate.html")
    

@app.route('/PirateReceiver', methods=['POST'])
def pirateparse():
    data = request.get_json()

@app.route('/navy')
def navy():
    return render_template("NPCs/Navy.html")

@app.route('/NavyReceiver', methods=['POST'])
def navyparse():    
    data = request.get_json()

@app.route('/China')
def china():
    global player
    this_region = Universe.getInstance().regions[0]
    if (player.region.getName() is not 'China'):
        trav = player.travel(this_region)
    if trav == "Trader":
        return redirect(url_for('trader'))
    elif trav == "Pirate":
        return redirect(url_for('pirate'))
    elif trav == "Navy":
        return redirect(url_for('navy'))
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[0].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/China.html", region_info=region_info)

@app.route('/India')
def india():
    global player
    this_region = Universe.getInstance().regions[1]
    if (player.region.getName() is not 'India'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[1].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/India.html", region_info=region_info)

@app.route('/Denmark')
def denmark():
    global player
    this_region = Universe.getInstance().regions[2]
    if (player.region.getName() is not 'Denmark'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[2].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Denmark.html", region_info=region_info)

@app.route('/Britain')
def britain():
    global player
    this_region = Universe.getInstance().regions[3]
    if (player.region.getName() is not 'Britain'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[3].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Britain.html", region_info=region_info)

@app.route('/Egypt')
def egypt():
    global player
    this_region = Universe.getInstance().regions[4]
    if (player.region.getName() is not 'Egypt'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[4].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Egypt.html", region_info=region_info)

@app.route('/Somalia')
def somalia():
    global player
    this_region = Universe.getInstance().regions[5]
    if (player.region.getName() is not 'Somalia'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[5].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Somalia.html", region_info=region_info)

@app.route('/Persia')
def persia():
    global player
    this_region = Universe.getInstance().regions[6]
    if (player.region.getName() is not 'Persia'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[6].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Persia.html", region_info=region_info)

@app.route('/Java')
def java():
    global player
    this_region = Universe.getInstance().regions[7]
    if (player.region.getName() is not 'Java'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[7].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Java.html", region_info=region_info)

@app.route('/Byzantium')
def byzantium():
    global player
    this_region = Universe.getInstance().regions[8]
    if (player.region.getName() is not 'Byzantium'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[8].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Byzantium.html", region_info=region_info)

@app.route('/Arabia')
def arabia():
    global player
    this_region = Universe.getInstance().regions[9]
    if (player.region.getName() is not 'Arabia'):
        trav = player.travel(this_region)
    if trav['enc'] == "Trader":
        return redirect(url_for('trader'), trav = trav)
    elif trav['enc'] == "Pirate":
        return redirect(url_for('pirate'), trav = trav)
    elif trav['enc'] == "Navy":
        return redirect(url_for('navy'), trav = trav)
    region_info = {'region_x' : this_region.getX(),
                   'region_y' : this_region.getY(),
                   'region_tech' : this_region.getTechLevel(),
                   'market' : this_region.market,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel}
    regions = Universe.getInstance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.getName()] = regions[9].get_fuel_cost(i.getX(), i.getY())
    region_info['fuel_costs'] = fuel_costs
    return render_template("Regions/Arabia.html", region_info=region_info)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

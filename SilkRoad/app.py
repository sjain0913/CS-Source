from flask import Flask, render_template, request, redirect, url_for, flash
from Universe import Universe
from Player import Player
from Pirates import Pirates
from Trader import Trader
from Game import Game
from Item import Item

app = Flask(__name__)
player = None
universe = None
game = None
trade = None

@app.route('/')
def title_screen():
    global player
    player = None
    global game
    game = None
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


@app.route('/config')
def config():
    global game
    difficulty = game.get_difficulty()
    skillpts = 0
    if difficulty == 1:
        skillpts = 16
    elif difficulty == 2:
        skillpts = 12
    else:
        skillpts = 8
    return render_template("Config.html", skillpts = skillpts)


@app.route('/playerdata')
def playerdata():
    skillpts = 0
    global game
    global player
    game.start_game()
    player.set_game(game)
    if game.get_difficulty() == 1:
        skillpts = 16
        player.credits = 1000
    elif game.get_difficulty() == 2:
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
    player_data = [player.name, player.credits, player.region.get_name(), player.sailor,
                   player.cannoneer, player.barterer, player.craftsman]
    return render_template("PlayerData.html", player_data = player_data)


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
    global trade
    global player
    trade = Trader(player)
    region_info = {'market' : trade.market.items,
                   'inventory' : player.inventory,
                   'fuel' : player.ship.fuel,
                   'health' : player.ship.health}
    return render_template("NPCs/Trader.html", region_info = region_info)

@app.route('/TraderReceiver', methods=['POST'])
def traderparse():
    data = request.get_json()
    choice = data['traderChoice']
    global trade
    if choice == "buy":
        trade.buy(data['itemBought'])
    elif choice == "sell":
        trade.sell(data['itemSold'])
    elif choice == "rob":
        trade.rob()
    else:
        trade.negotiate()

@app.route('/pirate')
def pirate():
    return render_template("NPCs/Pirate.html")


@app.route('/PirateReceiver', methods=['POST'])
def pirateparse():
    data = request.get_json()
    choice = data['pirateChoice']
    global player
    pir = Pirates(player)
    if choice == "pay":
        pir.pay()
    elif choice == "flee":
        pir.flee()
    else:
        pir.fight()

@app.route('/navy')
def navy():
    return render_template("NPCs/Navy.html")

@app.route('/NavyReceiver', methods=['POST'])
def navyparse():
    data = request.get_json()
    choice = data['navyChoice']
    return choice

@app.route('/MarketReceiver', methods=['POST'])
def marketparse():
    data = request.get_json()
    buy_item = data['itemBought']
    sell_item = data['itemSold']
    refuel = data['refuel']
    global player
    if buy_item != '':
        found = ''
        for item in player.region.market.items.values:
            if buy_item == item.name:
                found = item.name
        if found == '':
            flash('Cannot buy item not in the market')
            return redirect(url_for(player.region.__name))
        else:
            boughtItem = player.region.market.items[found] 
            player.credits = player.credits - boughtItem.buy_value
            player.region.market.remove_from_market(found)
            player.add_to_inv(found)
            return redirect(url_for(player.region.__name))
    elif sell_item != '':
        found = ''
        for item in player.inventory:
            if sell_item == item:
                found = item
        if found == '':
            flash('Cannot sell item not in your inventory')
            return redirect(url_for(player.region.__name))
        else:
            soldItem = player.inventory[found] 
            player.credits = player.credits + soldItem.sell_value
            player.region.market.add_to_market(found)
            player.remove_from_inv(found)
            return redirect(url_for(player.region.__name))
    elif refuel != 0:
        if refuel == 1:
            player.ship.fuel = player.ship.fuel + 1
            player.credits = player.credits - (2 * player.region.market.price_mult)
        elif refuel == 5:
            player.ship.fuel = player.ship.fuel + 5
            player.credits = player.credits - (10 * player.region.market.price_mult)
        elif refuel == "max":
            fuelcost = 2 * (player.ship.fuel_cap - player.ship.fuel)
            player.ship.fuel = player.ship.fuel_cap
            player.credits = player.credits - (fuelcost * player.region.market.price_mult)
    print(player.ship.fuel)

@app.route('/China')
def china():
    global player
    global game
    this_region = Universe.get_instance().regions[0]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[0].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'China':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/China.html", region_info=region_info)


@app.route('/India')
def india():
    global player
    this_region = Universe.get_instance().regions[1]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[1].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'India':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/India.html", region_info=region_info)


@app.route('/Denmark')
def denmark():
    global player
    this_region = Universe.get_instance().regions[2]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[2].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Denmark':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Denmark.html", region_info=region_info)


@app.route('/Britain')
def britain():
    global player
    this_region = Universe.get_instance().regions[3]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[3].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Britain':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Britain.html", region_info=region_info)


@app.route('/Egypt')
def egypt():
    global player
    this_region = Universe.get_instance().regions[4]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[4].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Egypt':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Egypt.html", region_info=region_info)


@app.route('/Somalia')
def somalia():
    global player
    this_region = Universe.get_instance().regions[5]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[5].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Somalia':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Somalia.html", region_info=region_info)


@app.route('/Persia')
def persia():
    global player
    this_region = Universe.get_instance().regions[6]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[6].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Persia':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Persia.html", region_info=region_info)


@app.route('/Java')
def java():
    global player
    this_region = Universe.get_instance().regions[7]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[7].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Java':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Java.html", region_info=region_info)


@app.route('/Byzantium')
def byzantium():
    global player
    this_region = Universe.get_instance().regions[8]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[8].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Byzantium':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Byzantium.html", region_info=region_info)


@app.route('/Arabia')
def arabia():
    global player
    this_region = Universe.get_instance().regions[9]
    market_list = {}
    for item in player.region.market.items.keys:
        market_list[item] = player.region.market.items[item].buy_value
    region_info = {'region_x' : this_region.getX(),
                'region_y' : this_region.getY(),
                'region_tech' : this_region.getTechLevel(),
                'market' : market_list,
                'inventory' : player.inventory,
                'fuel' : player.ship.fuel,
                'health' : player.ship.health}
    regions = Universe.get_instance().regions
    fuel_costs = {}
    for i in regions:
        fuel_costs[i.get_name()] = regions[9].get_fuel_cost(i.getX(), i.getY(), player)
    region_info['fuel_costs'] = fuel_costs
    if player.region.get_name() != 'Java':
        trav = player.travel(this_region, game)
    else:
        trav = {}
    if 'enc' in trav:
        if trav['enc'] == "Trader":
            return render_template('NPCs/Trader.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Pirate":
            return render_template('NPCs/Pirate.html', toRegion=trav['toRegion'])
        elif trav['enc'] == "Navy":
            return render_template('NPCs/Navy.html', toRegion=trav['toRegion'])
    else:
        this_region.market.populate_market(player)
        return render_template("Regions/Arabia.html", region_info=region_info)


if __name__ == '__main__':
    # app.debug = True
    app.run('0.0.0.0')

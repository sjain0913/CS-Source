from flask import Flask, render_template, request, session, redirect
import Player, Universe, Game, json

app = Flask(__name__)
player = None 
universe = None
game = None

@app.route('/')
def titleScreen():
    app.player = None
    return render_template('TitleScreen.html')


@app.route('/config')
def config():
    diff = app.game.getDifficulty()
    return render_template("Config.html", diff = json.dumps(diff))


@app.route('/diff')
def diff():
    return render_template("Difficulty.html")

@app.route('/playerdata')
def playerdata():
    playerData = [app.player.getSailor()]
    return render_template("PlayerData.html", playerData = map(json.dumps, playerData))


@app.route('/DifficultyReceiver', methods = ['POST'])
def difficultyparse():
    # read json + reply
    print(request)
    data = request.get_json()
    print(data)
    app.game = Game.Game(data['difficulty'])
    player = Player.Player(data['name'])

@app.route('/SkillReceiver', methods = ['POST'])
def skillparse():
    print(request)
    data = request.get_json()
    print(data)
    skillpts = 0
    if (app.game.getDifficulty() == 1):
        skillpts = 16
    elif (app.game.getDifficulty() == 2):
        skillpts = 12
    else:
        skillpts = 8
    

@app.route('/China')
def china():
    regionInfo = [Universe.Universe.getInstance().regions[0].getX(), Universe.Universe.getInstance().regions[0].getY(), Universe.Universe.getInstance().regions[0].getTechLevel()]
    return render_template("China.html", regionInfo = regionInfo)

@app.route('/India')
def india():
    regionInfo = [Universe.Universe.getInstance().regions[1].getX(), Universe.Universe.getInstance().regions[1].getY(), Universe.Universe.getInstance().regions[1].getTechLevel()]
    return render_template("India.html", regionInfo = regionInfo)

@app.route('/Denmark')
def denmark():
    regionInfo = [Universe.Universe.getInstance().regions[2].getX(), Universe.Universe.getInstance().regions[2].getY(), Universe.Universe.getInstance().regions[2].getTechLevel()]
    return render_template("Denmark.html", regionInfo = regionInfo)

@app.route('/Britain')
def britain():
    regionInfo = [Universe.Universe.getInstance().regions[3].getX(), Universe.Universe.getInstance().regions[3].getY(), Universe.Universe.getInstance().regions[3].getTechLevel()]
    return render_template("Britain.html", regionInfo = regionInfo)

@app.route('/Egypt')
def egypt():
    regionInfo = [Universe.Universe.getInstance().regions[4].getX(), Universe.Universe.getInstance().regions[4].getY(), Universe.Universe.getInstance().regions[4].getTechLevel()]
    return render_template("Egypt.html", regionInfo = regionInfo)

@app.route('/Somalia')
def somalia():
    regionInfo = [Universe.Universe.getInstance().regions[5].getX(), Universe.Universe.getInstance().regions[5].getY(), Universe.Universe.getInstance().regions[5].getTechLevel()]
    return render_template("Somalia.html", regionInfo = regionInfo)

@app.route('/Persia')
def persia():
    regionInfo = [Universe.Universe.getInstance().regions[6].getX(), Universe.Universe.getInstance().regions[6].getY(), Universe.Universe.getInstance().regions[6].getTechLevel()]
    return render_template("Persia.html", regionInfo = regionInfo)

@app.route('/Java')
def java():
    regionInfo = [Universe.Universe.getInstance().regions[7].getX(), Universe.Universe.getInstance().regions[7].getY(), Universe.Universe.getInstance().regions[7].getTechLevel()]
    return render_template("Java.html", regionInfo = regionInfo)

@app.route('/Byzantium')
def byzantium():
    regionInfo = [Universe.Universe.getInstance().regions[8].getX(), Universe.Universe.getInstance().regions[8].getY(), Universe.Universe.getInstance().regions[8].getTechLevel()]
    return render_template("Byzantium.html", regionInfo = regionInfo)

@app.route('/Arabia')
def arabia():
    regionInfo = [Universe.Universe.getInstance().regions[9].getX(), Universe.Universe.getInstance().regions[9].getY(), Universe.Universe.getInstance().regions[9].getTechLevel()]
    return render_template("Arabia.html", regionInfo = regionInfo)


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

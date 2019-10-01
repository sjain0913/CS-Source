from flask import Flask, render_template, request, session, redirect
import Config, json

app = Flask(__name__)


@app.route('/')
def titleScreen():
    return render_template('TitleScreen.html')


@app.route('/config')
def config():
    return render_template("Config.html")


@app.route('/diff')
def diff():
    return render_template("Difficulty.html")

@app.route('/playerdata')
def playerdata():
    return render_template("PlayerData.html")


@app.route('/receiver', methods = ['POST'])
def difficultyparse():
    # read json + reply
    print(request)
    data = request.get_json()
    print(data)
    config = Config.Config(data)
    config.to_String





if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

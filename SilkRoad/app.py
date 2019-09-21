from flask import Flask, render_template, request, session, redirect

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')

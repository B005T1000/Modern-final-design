import random
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load games from JSON file
def load_games():
    try:
        with open('games.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"games": [
            "The Legend of Zelda",
            "Super Mario Bros",
            "Minecraft",
            "Red Dead Redemption 2",
            "The Witcher 3",
            "God of War",
            "Grand Theft Auto V",
            "Portal 2",
            "Half-Life 2",
            "Dark Souls"
        ]}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick')
def pick_game():
    games = load_games()
    selected_game = random.choice(games["games"])
    return jsonify({"game": selected_game})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import os
import random
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Load games from JSON file. Support two categories: video and board (family) games.
def load_games():
    try:
        with open('games.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # fallback defaults
        data = {
            "video_games": [
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
            ],
            "board_games": [
                "Monopoly",
                "Catan",
                "Ticket to Ride",
                "Codenames",
                "Pandemic",
                "Carcassonne",
                "Uno",
                "Scrabble",
                "Chess",
                "Clue"
            ]
        }

    # Normalize older single-key format {"games": [...]} to video_games
    if 'games' in data and 'video_games' not in data:
        data = {
            'video_games': data.get('games', []),
            'board_games': data.get('board_games', [])
        }

    # Ensure keys exist
    data.setdefault('video_games', [])
    data.setdefault('board_games', [])
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick')
def pick_game():
    """Pick a random game. Query param `type` accepts 'video' or 'board'."""
    games = load_games()
    kind = request.args.get('type', 'video').lower()
    if kind in ('video', 'video_game', 'video_games'):
        pool = games.get('video_games', [])
        kind = 'video'
    elif kind in ('board', 'board_game', 'board_games', 'family'):
        pool = games.get('board_games', [])
        kind = 'board'
    else:
        return jsonify({'error': 'unknown type'}), 400

    if not pool:
        return jsonify({'error': 'no games available for type', 'type': kind}), 404

    selected_game = random.choice(pool)
    return jsonify({"game": selected_game, "type": kind})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
# Random Game Picker

A simple web application that helps you pick a random game to play from a predefined list.

## Features

- Randomly selects a game from a JSON list
- Simple and clean web interface
- Docker support for easy deployment
- Easily customizable game list

## Setup and Running

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t random-game-picker .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 random-game-picker
   ```

3. Access the application at: http://localhost:5000

### Without Docker

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Access the application at: http://localhost:5000

## Customizing Games

To add or modify games, edit the `games.json` file. The file contains a JSON array of game titles under the "games" key.

## Technical Stack

- Python 3.9
- Flask
- Docker
- HTML/CSS/JavaScript
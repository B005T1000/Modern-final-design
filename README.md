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

2. Run the container (use an available host port; example uses 5001):
   ```bash
   docker run -p 5001:5000 random-game-picker
   ```

3. Access the application at: http://localhost:5001

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

If the default port 5000 is in use, run with a different port:
```bash
# run on port 5001
PORT=5001 python3 app.py
```

Health check endpoint:

After the app is running you can check a lightweight health endpoint:
```bash
curl http://localhost:5000/healthz
# or if you used PORT=5001
curl http://localhost:5001/healthz
```

## Customizing Games

To add or modify games, edit the `games.json` file. The file contains a JSON array of game titles under the "games" key.

## Technical Stack

- Python 3.9
- Flask
- Docker
- HTML/CSS/JavaScript

## Deploying to Google Cloud (Cloud Run)

This project is packaged as a Docker container and can be deployed to Google Cloud Run. Below are the basic steps; replace PROJECT_ID, REGION, and SERVICE_NAME with your values.

1. Set your project and enable required APIs:
```bash
gcloud config set project PROJECT_ID
gcloud services enable cloudbuild.googleapis.com run.googleapis.com
```

2. Build and push the image with Cloud Build (recommended):
```bash
gcloud builds submit --config=cloudbuild.yaml --substitutions _SERVICE_NAME=game-picker,_REGION=us-central1
```

3. Or build and push manually, then deploy to Cloud Run:
```bash
docker build -t gcr.io/PROJECT_ID/random-game-picker .
docker push gcr.io/PROJECT_ID/random-game-picker
gcloud run deploy game-picker --image gcr.io/PROJECT_ID/random-game-picker --region us-central1 --platform managed --allow-unauthenticated
```

Notes:
- Ensure billing is enabled on the GCP project and you have the required IAM permissions (Cloud Run Admin, Storage Admin or Artifact Registry permissions, and Cloud Build Editor).
- The `cloudbuild.yaml` provided in the repo automates build+deploy using substitutions for `_SERVICE_NAME` and `_REGION`.
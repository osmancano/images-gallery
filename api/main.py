from flask import Flask, request
import requests
import os
from dotenv import load_dotenv 

load_dotenv(dotenv_path="./.env.local")

app = Flask(__name__)

UNSPLASH_URL='https://api.unsplash.com/photos/random/'
UNSPLASH_KEY = os.environ.get('UNSPLASH_KEY','')
if not UNSPLASH_KEY:
  raise EnvironmentError("Please .env.local file and insert there UNSPLASH_KEY.")

@app.route("/new-image")
def new_image():
    word = request.args.get('query')
    headers = {
      "Authorization" : "Client-ID " + UNSPLASH_KEY,
      "Accept-Verstion": "v1"
    }
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
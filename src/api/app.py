from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__, template_folder='../../templates')

# Configuration de la base de données
connection_str = "mongodb://azprojdb:P4VfpgpN5ggdPc3fJEuzSm3vOxYU6U2hNCi6edieJP4lCGGlJ5k7HONGdXbWkrNQgKiu6qhwjc4QACDbpkNDYQ==@azprojdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azprojdb@"
client = MongoClient(connection_str)
db = client.WeatherDB
container = db.WeatherData

@app.route('/')
def index():
    # Récupération de toutes les données
    all_data = list(container.find({}))
    
    return render_template('index.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

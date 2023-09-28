from flask import Flask, jsonify
from azure.cosmos import CosmosClient

app = Flask(__name__)

url = 'YOUR_COSMOS_DB_URL'  # Remplacez par votre URL
key = 'YOUR_COSMOS_DB_KEY'  # Remplacez par votre clé
database_name = 'YOUR_DATABASE_NAME'
container_name = 'YOUR_CONTAINER_NAME'
client = CosmosClient(url, credential=key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

@app.route('/data', methods=['GET'])
def get_data():
    data = list(container.query_items(
        query="SELECT * FROM c ORDER BY c._ts DESC",
        enable_cross_partition_query=True
    ))
    if data:
        return jsonify(data[0])
    else:
        return jsonify({"error": "Data not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)

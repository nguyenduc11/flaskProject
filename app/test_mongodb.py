from pymongo import MongoClient

# Replace the following with your MongoDB URI
uri = (
    "mongodb+srv://nguyenduc11:NJtdKiz5DQDU4HE2@clusterflaskweb.refwjuv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFlaskWeb")

try:
    client = MongoClient(uri)
    db = client.test
    db.command("ping")
    print("Database connection established.")
except Exception as e:
    print(f"Failed to connect to database: {e}")

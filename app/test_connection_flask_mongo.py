from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure

def test_and_explore_mongodb(app):
    try:
        # Create a new PyMongo instance
        mongo = PyMongo(app)

        # Send a ping to confirm a successful connection
        mongo.db.command('ping')
        print("Successfully connected to MongoDB!")

        # List all databases
        print("\nDatabases:")
        databases = mongo.db.list_database_names()
        for db in databases:
            print(f"- {db}")

            # List collections for each database
            db_obj = mongo.cx[db]
            collections = db_obj.list_collection_names()
            if collections:
                print("  Collections:")
                for collection in collections:
                    print(f"  - {collection}")
            else:
                print("  No collections found.")
            print()  # Empty line for readability

        return True
    except ConnectionFailure:
        print("Failed to connect to MongoDB.")
        return False

if __name__ == "__main__":
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://nguyenduc11:NJtdKiz5DQDU4HE2@clusterflaskweb.refwjuv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFlaskWeb"
    test_and_explore_mongodb(app)
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def test_and_explore_mongodb(uri):
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri)

        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")

        # List all databases
        print("\nDatabases:")
        databases = client.list_database_names()
        for db in databases:
            print(f"- {db}")

            # List collections for each database
            db_obj = client[db]
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
    finally:
        # Close the connection
        client.close()


# Usage example
if __name__ == "__main__":
    mongodb_uri = "mongodb+srv://nguyenduc11:NJtdKiz5DQDU4HE2@clusterflaskweb.refwjuv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFlaskWeb"
    test_and_explore_mongodb(mongodb_uri)
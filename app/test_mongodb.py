from pymongo import MongoClient

# Replace the following with your MongoDB URI
uri = ("mongodb+srv://atlasadmin:BseouAiAnmd5FOy1@cluster0.jp5bm2w.mongodb.net/?retryWrites=true&w=majority&appName"
       "=Cluster0")

try:
    client = MongoClient(uri)
    db = client.test
    db.command("ping")
    print("Database connection established.")
except Exception as e:
    print(f"Failed to connect to database: {e}")

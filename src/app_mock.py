from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db_connection = client['animedb']

collection = db_connection.get_collection('anime_rank')
# print(collection)

# collection.drop() # drop all documents into collection

# names = ["Lucas", "Renan", "Maues", "Nunes"]
# for name in names:
#     collection.insert_one({
#         "name": name,
#         "age": 26
#     })

for x in collection.find({}):
    print(x)

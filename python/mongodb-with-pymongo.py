def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    # CONNECTION_STRING = "mongodb+srv://root:example@localhost/myFirstDatabase"
    CONNECTION_STRING = "mongodb://root:example@localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']

def insert_sample_data(collection):
    item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
    }

    item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
    }
    collection.insert_many([item_1,item_2])
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    print("DB: {}, collection_name: {}".format(dbname, collection_name))
    insert_sample_data(collection_name)

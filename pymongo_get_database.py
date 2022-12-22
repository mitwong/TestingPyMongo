from pymongo import MongoClient
def get_database():

    CONNECTION_STRING = "mongodb+srv://admin:c6G7h8xkMHaC64qLHhuoWpAekUq9Je@cluster0.x5qs00a.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']

if __name__ == "__main__":

    dbname = get_database()
from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local

#Base de datos remota
db_client = MongoClient("mongodb+srv://FrancoCirielli:Franco2002@cursopython.oncfu3d.mongodb.net/?retryWrites=true&w=majority").test
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
class DBConnectionHandler:
    def __init__(self) -> None:
        self.connection_string = "mongodb://{}:{}".format(
            os.getenv("HOST"),
            os.getenv("PORT")
        )
        self.__database_name = os.getenv("DB_NAME")
        self.__client = None
        self.__db_connection = None

    def connect_database(self):
        self.__client = MongoClient(self.connection_string)
        self.__db_connection = self.__client[self.__database_name]
        return self.__db_connection

from typing import Dict, List
from src.models.database.connection import DBConnectionHandler

class AnimeRepository:
    def __init__(self, collection_name: str, db_connection: DBConnectionHandler) -> None:
        # self.__db_connection: object = DBConnectionHandler().connect_database()
        self.__db_connection = db_connection
        self.__collection_name = collection_name

    def insert_document(self, document: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def drop_all(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.drop()
        return "All documents has been removed from database"

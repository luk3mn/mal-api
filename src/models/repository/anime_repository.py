from typing import Dict, List
from src.models.database.connection import DBConnectionHandler

class AnimeRepository:
    def __init__(self, collection_name: str) -> None:
        self.__db_connection = DBConnectionHandler().connect_database()
        self.__collection_name = collection_name

    def insert_document(self, document: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def drop_all(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.drop()
        return "All documents has been removed from database"

    def find_documents(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        documents = collection.find({}, {"_id":0})
        document_list = []
        for document in documents:
            document_list.append(document)
        return document_list

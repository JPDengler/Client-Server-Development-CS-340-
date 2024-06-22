from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30826
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("Connection to MongoDB successful!")
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")

    def create(self, data):
        """
        Insert a document into the specified collection.
        :param data: A dictionary containing key/value pairs to insert
        :return: True if successful insert, else False
        """
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                print(f"Document inserted with ID: {result.inserted_id}")
                return True if result.inserted_id else False
            except PyMongoError as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise ValueError("Data must be a non-empty dictionary")

    def read(self, query):
        """
        Query for documents in the specified collection.
        :param query: A dictionary containing key/value pairs to use for lookup
        :return: A list of documents matching the query, or an empty list if no matches found
        """
        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                result = list(cursor) if cursor else []
                print(f"Query returned {len(result)} documents.")
                return result
            except PyMongoError as e:
                print(f"Error querying documents: {e}")
                return []
        else:
            raise ValueError("Query must be a non-empty dictionary")
           
    def update(self, query, new_values):
        """
        Update documents in the specified collection.
        :param query: A dictionary containing key/value pairs to use for lookup
        :param new_values: A dictionary containing key/value pairs for the new values
        :return: The number of documents updated
        """
        if query is not None and isinstance(query, dict) and new_values is not None and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            raise ValueError("Query and new values must be non-empty dictionaries")
            
            
    def delete(self, query):
        """
        Delete documents in the specified collection.
        :param query: A dictionary containing key/value pairs to use for lookup
        :return: The number of documents deleted
        """
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"Error deleting documents: {e}")
                return 0
        else:
            raise ValueError("Query must be a non-empty dictionary")



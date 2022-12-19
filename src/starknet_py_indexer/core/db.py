import os
import pymysql
from dotenv import load_dotenv
load_dotenv()

class DatabaseHandler:
    """Database Handler for StarkNet Indexer

    Parameter
    ---------
    host: str
        host address of the Database
    user: str
        user name of the Database
    pwd: str
        password of the Database
    db_name: str
        database name
    port: int
        port address of the Database
    network: str
        StarkNet network used
    """
    def __init__(self, host, user, pwd, db_name, port=3306, network='testnet'):
        self.network = network
        self._connection = self._get_connection(host, user, pwd, port, db_name)

    def _get_connection(self, host, user, pwd, port, db_name):
        connection = pymysql.connect(host=host, user=user, port=port, password=pwd, database=db_name, 
            cursorclass=pymysql.cursors.DictCursor)
        return connection

    def close_connection(self):
        self._connection.close()

    def execute_query(self, query):
        try:
            cursor = self._connection.cursor()
            cursor.execute(query)
            self._connection.commit()
            return cursor
        except Exception as e:
            print(e)
            return None

    #@TODO: Setup Database functions

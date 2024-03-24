import mysql.connector
from util.db_property_util import PropertyUtil


class DBConnection:
    @staticmethod
    def get_connection(property_file):
        properties = PropertyUtil.get_property_string(property_file)
        if properties:
            try:
                connection = mysql.connector.connect(
                    host=properties['hostname'],
                    database=properties['dbname'],
                    user=properties['username'],
                    password=properties['password'],
                    port=properties['port']
                )
                print("Connection established successfully.")
                return connection
            except mysql.connector.Error as e:
                print(f"Error connecting to database: {e}")
        return None

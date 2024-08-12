class DBClient(self):
    """
    Abstract base class for database client.
    """

    def __init__(self, host, database, user, password):
        """
        Initalizes a new Database Client.

        Args:
            host ('str'): The hostname of the database.
            database ('str'): The database name.
            user ('str'): The user of the database.
            password ('str'): The password for the database.

        Returns:
            None
        """
        pass


    def connect(self, *args, **kwargs) -> bool:
        """
        This method connects to the specified database server.

        Args:
            Any

        Returns:
            bool: If connection is succesful.
        """
        pass


    def send_db_query(self, query_str) -> bool:
        """
        This method sends a specific query to the database.

        Args:
            query_str ('str'): The query string to send to the database.
        
        Returns:
            bool: If query was sent successfully
        """
        pass


    def __clean_query_string(self, query_string) -> str:
        """
        This method cleans the query string for safety

        Args:
            query_string ('str'): The query string to be cleaned

        Returns:
            query_string ('str'): The cleaned string value
        """
        pass
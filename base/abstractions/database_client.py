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


    def send_db_command(self, command_str) -> bool:
        """
        This method send a specific command to the database.

        Args:
            command_str ('str'): The command string to send to the database.
        
        Returns:
            bool: If command was sent successfully
        """
        pass
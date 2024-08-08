class DBCommunicator(self):
    """
    Abstract base class for database communicator.
    """

    def connect(self, db_connection_str) -> bool:
        """
        This method connects to the specified database server.

        Args:
            db_connection_str ('object'): Database connection string.

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
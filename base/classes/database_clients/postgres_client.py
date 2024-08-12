# This file contains the Postgres DBClient object implementation

import logging
from abstractions import DBClient
import psycopg

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

class PostgresClient(DBClient):
    """
    Concrete implementation of the DBCommunicator class for Postgres
    """

    def __init__(self, host: str='', database: str='', user: str='', password: str=''):
        """
        Initalizes a new Postgres Client

        Args:
            host ('str'): The hostname of the postgres database.
            database ('str'): The postgres database name.
            user ('str'): The user of the postgres database.
            password ('str'): The password for the postgres database.

        Returns:
            None
        """
        log.info("Initializing new postgres client")
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.env_file_path = None


    def __inject_db_credentials(self):
        """
        This internal method sets the database connection properties

        Args:
            None

        Returns:
            None
        """
        try:
            with open(self.env_file_path, "r") as env:
                for line in env:
                    if line == "POSTGRES_HOST":
                        self.host = line
                    if line == "POSTGRES_DB":
                        self.database = line
                    if line == "POSTGRES_USER":
                        self.user = line
                    if line == "POSTGRES_PW":
                        self.password = line
        except Exception as err:
            raise RuntimeError(
                f"Setting database credentials failed with err: {err}"
            )


    def connect(self) -> bool:
        """
        This method connects to the specified postgres server.

        Args:
            None

        Returns:
            bool: If connection is succesful.
        """
        log.info(f"Connecting to {self.database}")

        if self.connection:
            self.connection.close()

        try:
            self.__inject_db_credentials()

            self.connection = psycopg.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            log.info(f"Connected to {self.database} successfully!")
            
            return True
            
        except Exception:
            raise RuntimeError(
                f"Failed to connect {self.database}!"
            )


    def send_db_query(self, query_str) -> bool:
        """
        This method sends a specific query to the database.

        Args:
            query_str ('str'): The query string to send to the database.
        
        Returns:
            bool: If query was sent successfully
        """
        if not self.cursor:
            try:
                self.connect()
            except Exception:
                raise RuntimeError(
                    f"Failed to connect {self.database}!"
                )
        
        try:
            self.cursor.execute(query_str)
            self.cursor.commit()
        
        except Exception as err:
            raise RuntimeError(
                f"Transaction failed with error: {err}"
            )


    def __clean_query_string(self, query_string) -> str:
        """
        This method cleans the query string for safety

        Args:
            query_string ('str'): The query string to be cleaned

        Returns:
            query_string ('str'): The cleaned string value
        """
        pass
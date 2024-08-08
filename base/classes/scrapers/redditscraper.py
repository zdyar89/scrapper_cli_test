# This file contains the Reddit DataScaper object implementation

import logger
import requests
from bs4 import BeautifulSoup

class RedditDataScraper(DataScraper):
    """
    Concrete implementation of the DataScraper class for scraping data from Reddit.
    """

    def __init__(
        self, api_key_uri: str, api_key: str='', connection: bool=False
    ) -> None:
        """
        Initializes a new RedditDataScraper object.

        Args:
            api_key_uri ('str'). The
            api_key ('str'): The Reddit api key.
            connection ('str'): The connection status.
        
        Returns:
            None
        """
        self.api_key_uri = api_key_uri
        self.api_key = api_key
        self.connection = connection


    def _set_api_key(self):
        """
        This internal method sets the Reddit api key property.

        Args:
            None

        Returns:
            None
        """
        try:
            self.api_key = self.api_key_uri
            log.info(f"Api key is set")
        except Exception as err:
            raise RuntimeError(
                f"Setting api key failed with error: {err}"
            )


    def connect(self) -> bool:
        """
        This method connects to the Reddit api.

        Args:
            None

        Returns:
            bool: If connection is successful.
        """
        if self.api_key == '':
            try:
                _set_api_key()
            except Exception as err:
                raise RuntimeError(
                    f"Setting api key failed with error: {err}"
                )

        try:
            # test connection logic here
            # self.connection = True
        except Exception as err:
            raise RuntimeError(
                f"Reddit api connection failed with error: {err}"
            )


    def api_pull_data(self, query_str: str):
        """
        This method pulls data from the api endpoint.

        Args:
            query_str ('str'): The api query string.
        
        Returns:
            object: The returned data object.
        """
        if not self.connection:
            try:
                connect(self.api_key)
            except Exception as err:
                raise RuntimeError(
                    f"Reddit api connection failed with error: {err}"
                )

        try:
            # api pull logic here
        except Exception as err:
            raise RuntimeError(
                f"Api query failed with error: {err}"
            )
            

    def scrape_data(self, url):
        """
        This method scrapes data from the given Reddit URL.
        
        Args:
            url ('str'): The Reddit URL to scrape data from.
        
        Returns:
            object: The scraped Reddit data object.
        """


    def clean_data(self, data: object) -> object:
        """
        This method cleans the scraped Reddit data.
        
        Args:
            data ('object'): The scraped Reddit data object.
        
        Returns:
            object: The cleaned Reddit data object.
        """


    def save_data(self, data, output_file) -> bool:
        """
        This method saves the cleaned data to a file.
        
        Args:
            data ('object'): The cleaned Reddit data.
            output_file ('str'): The path to the output file.

        Returns:
            bool: If Reddit is saved successfully
        """

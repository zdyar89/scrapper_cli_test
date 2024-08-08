class DataScraper(self):
    """
    Abstract base class for data scrapers.
    """

    def __init__(
        self, api_key_uri: str, api_key: str='', connection: bool=False
    ) -> None:
        """
        Initializaes a new DataScraper object.

        Args:
            api_key_uri ('str'): The api key.
            api_key ('str'): The api key.
            connection ('bool'): The connection status.

        Returns:
            None
        """
        pass


    def _set_api_key(self) -> None:
        """
        This internal method sets the api key property.

        Args:
            None

        Returns:
            None
        """
        pass


    def connect(self) -> bool:
        """
        This method connects to the specified api with a valid key.

        Args:
            None

        Returns:
            bool: If connection was successful.
        """
        pass


    def api_pull_data(self, query_str) -> object:
        """
        This method pulls data from the api endpoint.

        Args:
            query_str ('str'): The api query string.
        
        Returns:
            object ('object'): The returned data object.
        """
        pass


    def scrape_data(self, url) -> object:
        """
        This method scrapes data from the given URL.
        
        Args:
            url ('str'): The URL to scrape data from.
        
        Returns:
            object ('object'): The scraped data object.
        """
        pass


    def clean_data(self, data) -> object:
        """
        This method cleans the scraped data.
        
        Args:
            data ('object'): The scraped data object.
        
        Returns:
            object ('object'): The cleaned data object.
        """
        pass


    def save_data(self, data, output_file) -> bool:
        """
        This method saves the cleaned data to a file.
        
        Args:
            data ('object'): The cleaned data object.
            output_file ('str'): The path to the output file.

        Returns:
            bool: If data is saved successfully
        """
        pass
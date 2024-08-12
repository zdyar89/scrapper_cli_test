"""
    Unit test cases for postgres db client
"""

import pytest
from database_clients import PostgresClient
from database_clients.postgres_client import(
    connect,
    send_db_query
)

pg_client = PostgresClient()

def create_pg_client() -> object:
    """
    mocks PostgresClient object
    Returns:
        pg_client: object
    """
    pg_client = PostgresClient(

    )
    return pg_client

def test_connect(mocker) -> bool:
    """
    Unit test case for connect() function
    """
    mocker.patch(pg_client)


def test_send_db_query(mocker) -> bool:
    """
    Unit test case for send_db_query() function
    """
    mocker.patch(pg_client)


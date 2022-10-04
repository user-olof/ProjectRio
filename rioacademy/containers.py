from dependency_injector import containers, providers
import sqlite3

from . import services

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Gateways

    database_client = providers.Singleton(sqlite3.connect)

    # Services

    
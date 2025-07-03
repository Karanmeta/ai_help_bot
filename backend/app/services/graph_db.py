from neo4j import GraphDatabase, exceptions
from ..core.config import settings
import time

class Neo4jGraph:
    def __init__(self):
        self.driver = None
        retries = 5
        while retries > 0:
            try:
                self.driver = GraphDatabase.driver(settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD))
                self.driver.verify_connectivity()
                print("Successfully connected to Neo4j.")
                break
            except exceptions.ServiceUnavailable:
                retries -= 1
                print(f"Neo4j not available, retrying... ({retries} retries left)")
                time.sleep(5)
        if not self.driver:
            raise ConnectionError("Could not connect to Neo4j.")

    def run_query(self, query: str, parameters: dict = None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]

graph_db_connection = Neo4jGraph()
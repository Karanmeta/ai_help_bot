import json
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth

# --- Configuration ---
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "all_extracted_kg.json")

def load_data(uri, user, password, file_path):
    driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    with driver.session() as session:
        # Create a uniqueness constraint to avoid duplicate nodes
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (n:Entity) REQUIRE n.name IS UNIQUE")
        print("Uniqueness constraint ensured for :Entity(name).")

        # Load the JSON data
        try:
            with open(file_path, 'r') as f:
                data_dict = json.load(f)
            print(f"Successfully loaded JSON data with {len(data_dict)} main keys.")
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return

        print("Starting to load knowledge graph into Neo4j...")
        total_triples = 0
        
        # The main data is a dictionary where values are lists of triples
        for key, list_of_triples in data_dict.items():
            if not isinstance(list_of_triples, list):
                print(f"Skipping key '{key}' as its value is not a list.")
                continue

            for triple in list_of_triples:
                # Ensure the triple is a list with exactly 3 elements
                if isinstance(triple, list) and len(triple) == 3:
                    head, relation, tail = triple
                    
                    # Ensure all parts are strings to prevent errors
                    head = str(head)
                    relation = str(relation)
                    tail = str(tail)

                    # Create nodes and relationship in Neo4j
                    query = """
                    MERGE (h:Entity {name: $head})
                    MERGE (t:Entity {name: $tail})
                    MERGE (h)-[r:RELATIONSHIP {type: $relation}]->(t)
                    """
                    session.run(query, head=head, tail=tail, relation=relation)
                    total_triples += 1
                else:
                    print(f"Skipping malformed triple: {triple}")

                if total_triples > 0 and total_triples % 100 == 0:
                    print(f"Processed {total_triples} triples so far...")
    
    print(f"\nData loading complete. A total of {total_triples} triples were processed.")
    driver.close()

if __name__ == "__main__":
    if not all([NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD]):
        print("Error: Neo4j credentials not found in .env file.")
    else:
        load_data(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, JSON_FILE_PATH)
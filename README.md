# AI-Based Help Bot for MOSDAC

This project is a full-stack AI chatbot built to interact with data from MOSDAC. It uses a microservices architecture, containerized with Docker for easy setup and deployment.

### How to Run

1.  **Create your environment file:**
    Copy `.env.example` to a new file named `.env`.
    ```bash
    cp .env.example .env
    ```

2.  **Edit `.env`:**
    Open the newly created `.env` file and add your `NEO4J_PASSWORD` and your `HUGGINGFACEHUB_API_TOKEN`.

3.  **Build and run the services:**
    This command will build and start all services.
    ```bash
    docker-compose up --build
    ```

### Accessing the Services

- **Chatbot UI**: `http://localhost:3000`
- **Backend API Docs**: `http://localhost:8000/docs`
- **Neo4j Browser**: `http://localhost:7474` (Log in with user `neo4j` and the password from your `.env` file)

### Initial Data Setup for Neo4j

After starting the services, go to the Neo4j Browser, log in, and run the following Cypher query to create sample data so the graph tool will work.
```cypher
CREATE (isro:Organization {name: 'ISRO'}),
       (insat:Satellite {name: 'INSAT-3D'}),
       (rainfall:Product {name: 'Rainfall Product', update_frequency: '15 minutes'}),
       (cloud:Product {name: 'Cloud Mask'}),
       (isro)-[:MANAGES]->(insat),
       (insat)-[:PROVIDES]->(rainfall),
       (insat)-[:PROVIDES]->(cloud)
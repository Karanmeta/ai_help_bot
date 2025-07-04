from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_huggingface import HuggingFaceHub
from langchain.prompts import PromptTemplate

# Initialize the Neo4j graph connection from environment variables
# This will use the same .env file as your docker-compose setup
graph_db_connection = Neo4jGraph()

# Refresh the schema to make sure the agent knows about the loaded data
print("Refreshing graph schema...")
graph_db_connection.refresh_schema()
print("Graph schema refreshed.")

# Define the language model from Hugging Face
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    model_kwargs={"temperature": 0.5, "max_length": 1024}
)

# Create a more descriptive prompt to guide the LLM
CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j developer and data analyst for MOSDAC satellite data.
Your task is to convert a user's question in natural language into a Cypher query to answer the question from a Neo4j database.

The user is asking questions about satellites, sensors, and their data products.
Use only the provided relationship types and properties in the schema. Do not use any other relationship types or properties that are not provided.

Schema:
{schema}

Here are some examples of the kind of nodes and relationships you might see:
- Nodes are of type `:Entity`. They have a `name` property. Examples: (e:Entity {{name: 'Oceansat-2'}}), (e:Entity {{name: 'OCM'}})
- Relationships are of type `:RELATIONSHIP`. They have a `type` property. Examples: [r:RELATIONSHIP {{type: 'has sensor'}}], [r:RELATIONSHIP {{type: 'provides data'}}]

Question:
{question}

Cypher Query:
"""

CYPHER_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], 
    template=CYPHER_GENERATION_TEMPLATE
)

# Initialize the LangChain Cypher QA Chain
agent_executor = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph_db_connection,
    cypher_prompt=CYPHER_PROMPT,
    verbose=True, # Set to True to see the generated Cypher queries in the logs
    return_intermediate_steps=True # Useful for debugging
)
import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_community.llms import HuggingFaceHub
from langchain import hub
from ..core.config import settings
from .vector_store import get_vectorstore_retriever
from .graph_db import graph_db_connection
from langchain.chains import RetrievalQA

os.environ["HUGGINGFACEHUB_API_TOKEN"] = settings.HUGGINGFACEHUB_API_TOKEN

def create_agent_executor():
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.2, "max_new_tokens": 1024}
    )
    retriever = get_vectorstore_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    rag_tool = Tool(
        name="Document Search",
        func=qa_chain.invoke,
        description="Best for answering questions about product descriptions, missions, update frequencies, and general descriptive topics. Use a full question as input."
    )
    def run_graph_query(query: str) -> str:
        try:
            result = graph_db_connection.run_query(query)
            return str(result)
        except Exception as e:
            return f"Error executing Cypher query: {e}. Please check syntax."
    graph_tool = Tool(
        name="Knowledge Graph Search",
        func=run_graph_query,
        description="Use this for specific factual queries about relationships between entities like Satellites, Products, and Organizations. Input MUST be a valid Cypher query."
    )
    tools = [rag_tool, graph_tool]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    print("Agent created successfully.")
    return agent_executor

agent_executor = create_agent_executor()
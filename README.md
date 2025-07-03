# Full-Stack AI Chatbot with LangChain, React, and Neo4j

This project is a full-stack, containerized AI chatbot built to interact with a Neo4j graph database. It uses a React frontend, a Python FastAPI backend, and LangChain for orchestrating the AI agent.

![Chatbot Screenshot](https://raw.githubusercontent.com/AI-Citizen/fullstack-ai-chatbot-langchain-react/main/docs/screenshot.png)

## Features

-   **Natural Language Queries:** Ask questions in plain English to query the database.
-   **Full-Stack Architecture:** A complete separation of concerns between the React frontend and the FastAPI backend API.
-   **Graph Database Integration:** Connects to a Neo4j database to store and retrieve graph-based data.
-   **Dockerized Environment:** The entire application stack (frontend, backend, database) is managed with Docker for easy, one-command setup.

## Tech Stack

-   **Frontend:** React
-   **Backend:** Python with FastAPI
-   **AI Orchestration:** LangChain
-   **LLM Provider:** Hugging Face
-   **Database:** Neo4j Graph Database
-   **Containerization:** Docker

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Docker Desktop:** The application runs entirely in Docker containers. [Download Docker Desktop](https://www.docker.com/products/docker-desktop/).
2.  **Git:** Required to clone the repository correctly. [Download Git](https://git-scm.com/downloads).

## Setup and Installation

Follow these steps carefully to get the application running.

### 1. Clone the Repository

First, clone the repository to your local machine using Git. **Do not download the ZIP file**, as this will not include the necessary Git history for updates.

```bash
git clone https://github.com/Karanmeta/ai_help_bot
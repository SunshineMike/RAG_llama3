# RAG with llama3

This project is a Python-based application that provides an interface for uploading PDF files and querying the stored information. It uses Flask as a web framework and leverages the llama3 open-source model for language understanding and the Chroma vector store for efficient data retrieval.

## Features

- **PDF Upload**: Upload your PDF files to the server. The content of the PDFs is processed and stored in a vector database.
- **Query Interface**: Query the content of your uploaded PDFs. The application uses a similarity score threshold to retrieve the most relevant documents.

## Getting Started

### Prerequisites

- Python
- pip

### Installation

1. Clone the repository
```bash
git clone <repository_url>
```
2. Navigate to the project directory
```bash
cd <project_directory>
```
3. Create a virtual environment
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate
```
3. Install the required Python packages
```bash
pip install -r requirements.txt
```
4. Run the setup script for Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
5. Pull the Ollama model
```bash
ollama pull llama3
```
6. Verify 
```bash
ollama list
ollama run llama3
'Hy AI!'
'/bye'
```

## Usage

1. Start the application
```bash
python3 app.py
```
2. The application is now running at `localhost:8080`. You can interact with it using the following endpoints:

- `POST /ai`: Send a chat message to the AI model.
- `POST /rag`: Query the vector database.
- `POST /pdf`: Upload a PDF file.

### API
[API Documentation](documentation/API%20Documentation.md)

![Example Image](images/logo.png)

This project is a Python-based application that provides an interface for uploading PDF files and querying the stored information. It uses Flask as a web framework and utilizes the open source llama3 model for language understanding and chroma vector memory for efficient data retrieval. The system prompt in this setup aims to extract and summarize information in various PDFs. The agent uses a pattern called “extract_wisdom” from Daniel Miessler's 'Fabric'.
<br><br>Prompt: https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md

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
git clone https://github.com/SunshineMike/RAG_llama3.git
```
<br>

2. Navigate to the project directory
```bash
cd RAG_llama3
```
<br>

3. Create a virtual environment
```bash
python -m venv venv
```
<br>

4. Activate the virtual environment
```bash
source venv/bin/activate
```
<br>

3. Install the required Python packages
```bash
pip install -r requirements.txt
```
<br>

4. Run the setup script for Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
<br>

5. Pull the Ollama model
```bash
ollama pull llama3
```
<br>

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

For quick testing use **Postman**:
https://www.postman.com/



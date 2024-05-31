import os

from flask import Flask, request

from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate

from config.raw_prompt import RAW_PROMPT_WISDOM, RAW_PROMPT


app = Flask(__name__)
db_path = 'db'
llm = Ollama(model='llama3')

embedding = FastEmbedEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024,
                                               chunk_overlap=80,
                                               length_function=len,
                                               is_separator_regex=False)

raw_prompt = PromptTemplate.from_template(RAW_PROMPT)


@app.route("/ai", methods=['POST'])
def ai_post():
    print('POST /ai called!')
    json_content = request.get_json()
    query = json_content['query']
    response = {"text": llm.invoke(query)}
    return response, 200


@app.route("/rag", methods=['POST'])
def rag_post():
    print('POST /rag called!')
    json_content = request.get_json()
    query = json_content['query']

    vector_store = Chroma(persist_directory=db_path, embedding_function=embedding)

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 20,
            "score_threshold": 0.1,
        },
    )

    document_chain = create_stuff_documents_chain(llm, raw_prompt)
    chain = create_retrieval_chain(retriever, document_chain)
    response = chain.invoke({"input": query})

    print(response)
    sources = []
    for doc in response["context"]:
        sources.append(
            {"source": doc.metadata["source"], "page_content": doc.page_content}
        )

    return {"answer": response["answer"], "sources": sources}, 200


@app.route("/pdf", methods=['POST'])
def pdf_post():
    print('POST /pdf called!')
    file = request.files["file"]
    file_name = file.filename
    file_path = f'pdf/{file_name}'
    file.save(file_path)

    loader = PDFPlumberLoader(file_path)
    docs = loader.load_and_split()
    print(f'Loaded {len(docs)} documents')

    chunks = text_splitter.split_documents(docs)
    print(f'Splitted {len(chunks)} documents')

    vector_store = Chroma.from_documents(documents=chunks,
                                         embedding=embedding,
                                         persist_directory=db_path)
    vector_store.persist()

    print(f'File saved: {file_path}')
    response = {"status": "ok",
                "filename": file_path,
                "doc_len": len(docs),
                "chunks": len(chunks)}
    return response, 200


@app.route("/txt", methods=['POST'])
def txt_post():
    print('POST /txt called!')
    file = request.files["file"]
    file_name = file.filename
    file_path = f'txt/{file_name}'
    file.save(file_path)

    loader = TextLoader(file_path)
    docs = loader.load_and_split()
    print(f'Loaded {len(docs)} documents')

    chunks = text_splitter.split_documents(docs)
    print(f'Splitted {len(chunks)} documents')

    vector_store = Chroma.from_documents(documents=chunks,
                                         embedding=embedding,
                                         persist_directory=db_path)
    vector_store.persist()

    print(f'File saved: {file_path}')
    response = {"status": "ok",
                "filename": file_path,
                "doc_len": len(docs),
                "chunks": len(chunks)}
    return response, 200


def ensure_directories_exist():
    directories = ['db', 'pdf', 'txt']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def start_app():
    ensure_directories_exist()
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == '__main__':
    start_app()

# API Documentation
**HOST:** `localhost:8080`

## 1. Chat Endpoint

This endpoint is used to interact with the AI model.

**URL:** `/ai`

**Method:** `POST`

**Headers:**

- `Content-Type: application/json`

**Body:**

```json
{
    "query": "<Your Query Here>"
}
```

**Example:**

```http request
POST /ai HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{
    "query": "Hello, AI!"
}
```

## 2. Query Database Endpoint

This endpoint is used to query the database.

**URL:** `/rag`

**Method:** `POST`

**Headers:**

- `Content-Type: application/json`

**Body:**

```json
{
    "query": "<Your Query Here>"
}
```

**Example:**

```http request
POST /rag HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{
    "query": "What are this numbers mean?"
}
```

## 3. Upload Data (PDF) Endpoint

This endpoint is used to upload a PDF file.

**URL:** `/pdf`

**Method:** `POST`

**Headers:**

- `Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW`

**Body:**

The body should contain the PDF file data.

**Example:**

```http request
POST /pdf HTTP/1.1
Host: localhost:8080
Content-Length: 197
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="YourFile.pdf"
Content-Type: application/pdf

(data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

Replace `(data)` with the actual content of your PDF file.
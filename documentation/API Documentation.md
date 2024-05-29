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

```python
import requests
import json

url = "http://localhost:8080/ai"

payload = json.dumps({
  "query": "Hy AI!"
})
headers = {
  'A': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
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

```python
import requests
import json

url = "http://localhost:8080/rag"

payload = json.dumps({
  "query": "Ask your data!"
})
headers = {
  'A': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## 3. Upload Data (PDF) Endpoint

This endpoint is used to upload a PDF file.

**URL:** `/pdf`

**Method:** `POST`

**Example:**

```python
import requests

url = "http://localhost:8080/pdf"

payload = {}
files=[
  ('file',('your_file.pdf',open('path/to/your/file/your_file.pdf','rb'),'application/pdf'))
]
headers = {
  'A': ''
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

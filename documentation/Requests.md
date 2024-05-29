# Example Requests

## Chat
```http request
POST /ai HTTP/1.1
Host: localhost:8080
A: 
Content-Type: application/json
Content-Length: 22

{
    "query": "Hy!"
}
```


## Query database
```http request
POST /rag HTTP/1.1
Host: localhost:8080
A: 
Content-Type: application/json
Content-Length: 58

{
    "query": "What is the current mitigation process?"
}
```

## Upload data (pdf)
```http request
POST /pdf HTTP/1.1
Host: localhost:8080
A: 
Content-Length: 197
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="IPCC_AR6_SYR_SPM.pdf"
Content-Type: application/pdf

(data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
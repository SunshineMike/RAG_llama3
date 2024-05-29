# Setup Ollama

### Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```


### Load Model
```bash
ollama pull llama3
```


### List models
```bash
ollama list
```


### Start server
```bash
ollama serve
```

### Use Service
```bash
ollama run llama3
```
Talk to the Model


### Code
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Hy!",
  "stream": false
}'
```
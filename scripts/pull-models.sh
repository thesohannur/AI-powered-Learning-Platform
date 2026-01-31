#!/bin/bash
# Pull AI models into Ollama Docker container

echo "Pulling AI models into Ollama..."
echo "This will download ~10GB of models. It may take 10-20 minutes."
echo ""

# Pull models
echo "1/3 Pulling llama3.1:8b (4.7GB)..."
docker exec learning-platform-ollama ollama pull llama3.1:8b

echo ""
echo "2/3 Pulling nomic-embed-text (274MB)..."
docker exec learning-platform-ollama ollama pull nomic-embed-text

echo ""
echo "3/3 Pulling codellama:7b (3.8GB)..."
docker exec learning-platform-ollama ollama pull codellama:7b

echo ""
echo "✅ All models downloaded!"
echo ""
echo "Verify with: docker exec learning-platform-ollama ollama list"

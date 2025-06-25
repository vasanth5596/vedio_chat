#!/bin/bash
set -e  # Exit on error

echo "⏱️ Starting deployment..."

echo "🚫 Stopping old container (if any)..."
docker stop vedio_chat_container || true
docker rm vedio_chat_container || true

echo "🐳 Building Docker image..."
docker build -t vedio_chat .

echo "🏷️ Tagging image for Docker Hub..."
docker tag vedio_chat vasanth5596/vedio_chat:latest

echo "📤 Pushing image to Docker Hub..."
docker push vasanth5596/vedio_chat:latest

echo "🚀 Running the container..."
docker run -d -p 5000:5000 --name vedio_chat_container vasanth5596/vedio_chat:latest

echo "✅ Deployment completed and container running on port 5000"

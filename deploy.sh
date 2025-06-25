#!/bin/bash

# Build Docker image and tag for Docker Hub
docker build -t vedio_chat .
docker tag vedio_chat vasanth5596/vedio_chat:latest

# Push to Docker Hub
docker push vasanth5596/vedio_chat:latest

# Run the container (for testing)
docker run -d -p 80:80 --name vedio_chat_container vasanth5596/vedio_chat:latest

echo "Deployment completed on Docker Hub and container running locally."
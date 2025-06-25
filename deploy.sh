#!/bin/bash

# Build Docker image
docker build -t vedio_chat .

# Run the container (for testing)
docker run -d -p 80:80 --name vedio_chat_container vedio_chat

# Optional: Push to Docker Hub/ECR (configure accordingly)
# docker tag vedio_chat your_dockerhub_username/vedio_chat:latest
# docker push your_dockerhub_username/vedio_chat:latest

echo "Deployment completed"
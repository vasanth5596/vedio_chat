#!/bin/bash
set -e  # Exit on error

echo "⏱️ Starting deployment..."

ECR_REGISTRY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
ECR_REPOSITORY="video_chat"
IMAGE_TAG="latest"

echo "🚫 Stopping old container (if any)..."
ssh -i "your-key.pem" ec2-user@184.72.207.65 "docker stop vedio_chat_container || true && docker rm vedio_chat_container || true"

echo "📥 Pulling image from AWS ECR..."
ssh -i "your-key.pem" ec2-user@184.72.207.65 "docker pull ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"

echo "🚀 Running the container..."
ssh -i "your-key.pem" ec2-user@184.72.207.65 "docker run -d -p 5000:5000 --name vedio_chat_container ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"

echo "✅ Deployment completed and container running on port 5000"
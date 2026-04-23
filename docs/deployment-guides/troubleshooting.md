# Troubleshooting Guide

## Common Problems & Fixes:

### 1. Pods are in "Pending" state
- **Reason**: Not enough CPU/Memory in your cluster.
- **Fix**: Increase the node size or number of nodes.

### 2. "ImagePullBackOff" Error
- **Reason**: Kubernetes can't find your Docker image.
- **Fix**: Check if the image name is correct and if it's pushed to Docker Hub.

### 3. Connection Refused to Database
- **Reason**: Backend is trying to connect before the database is ready.
- **Fix**: Kubernetes will automatically restart the pod until it connects.

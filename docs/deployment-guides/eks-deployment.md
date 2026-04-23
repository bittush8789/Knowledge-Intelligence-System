# AWS EKS Deployment Guide

Deploy your application to the cloud using Amazon EKS.

## 1. Configure AWS CLI
```bash
aws configure
```
Enter your AWS Access Key, Secret Key, and Region (e.g., `ap-south-1`).

## 2. Create the EKS Cluster
Using `eksctl` is the easiest way:
```bash
eksctl create cluster \
--name ai-platform \
--region ap-south-1 \
--nodes 2 \
--node-type t3.medium
```
*Note: This might take 15-20 minutes.*

## 3. Connect to the Cluster
```bash
aws eks update-kubeconfig --name ai-platform --region ap-south-1
```

## 4. Deploy the Application
```bash
kubectl apply -f k8s-simple/
```

## 5. Get the LoadBalancer URL
```bash
kubectl get svc -n ai-platform
```
Look for the `EXTERNAL-IP` of the `app-ingress` or LoadBalancer service.

## 6. Delete Cluster (To save money!)
```bash
eksctl delete cluster --name ai-platform --region ap-south-1
```

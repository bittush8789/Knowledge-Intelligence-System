#!/bin/bash
# Script to destroy all resources

echo "🗑️ Destroying all resources..."

kubectl delete -f .
kubectl delete namespace ai-platform

echo "✅ Cleanup finished!"

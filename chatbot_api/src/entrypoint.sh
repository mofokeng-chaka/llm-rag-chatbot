#!/bin/bash

rm /app/data/etl_complete

#echo "Waiting for ETL completion..."
#while [ ! -f /app/data/etl_complete ]; do
#  sleep 5
#done

# Run any setup steps or pre-processing tasks here
echo "Starting SALT RAG FastAPI service..."

# Start the main application
uvicorn main:app --host 0.0.0.0 --port 8001
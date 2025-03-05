#!/bin/sh

# Start FastAPI in the background
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit
streamlit run fe/web_app.py --server.port 8501 --server.address 0.0.0.0

FROM python:3.12.8

# Set the working directory
WORKDIR /main_image_app/

# Copy dependencies
COPY ./requirements.txt /main_image_app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /main_image_app/requirements.txt

# Copy source code
COPY ./src /main_image_app/src
COPY ./fe /main_image_app/fe

# # Copy the database file (if needed)
# COPY ./dbteste.db /main_image_app/dbteste.db

# Expose required ports
EXPOSE 8000
EXPOSE 8501

# Use a process manager to run both FastAPI and Streamlit
# CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port 8000 & streamlit run fe/web_app.py --server.port 8501 --server.address 0.0.0.0"]

# Copy and use a script to start both FastAPI and Streamlit
COPY start.sh /main_image_app/start.sh
RUN chmod +x /main_image_app/start.sh

CMD ["/main_image_app/start.sh"]
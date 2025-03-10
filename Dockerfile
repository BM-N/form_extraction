FROM python:3.12.8

# Set the working directory
WORKDIR /main_image_app/

# Copy dependencies
COPY ./requirements.txt /main_image_app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /main_image_app/requirements.txt

# Copy source and fe code
COPY ./src /main_image_app/src
COPY ./fe /main_image_app/fe

# # Copy the database file (if needed)
# COPY ./dbteste.db /main_image_app/dbteste.db

# Expose required ports
EXPOSE 8000
EXPOSE 8501

# script to start both FastAPI and Streamlit
COPY start.sh /main_image_app/start.sh
RUN chmod +x /main_image_app/start.sh

CMD ["/main_image_app/start.sh"]
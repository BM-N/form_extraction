# Healthcare Form Data Extraction App

## Overview

This application extracts data from healthcare form images (.pdf, .png, .jpeg) using OCR and processes it into structured JSON format, storing it in a database. It includes a Streamlit interface, a FastAPI backend, EasyOCR for text extraction, and database integration via SQLAlchemy, all containerized with Docker.

## Features

*   Accepts .pdf, .png, .jpeg form images.
*   Automated text extraction with EasyOCR.
*   Intelligent text processing and data structuring.
*   JSON output based on Pydantic models.
*   Database storage using SQLAlchemy.
*   Docker containerized for deployment.

## Requirements

*   Python 3.8+
*   Docker (for containerization)
*   Uv (for dependencies and venv management. Optional but recommended.)

**Python Dependencies:**  Check out `requirements.txt`.

## Installation and Setup

### Local Setup

1.  Clone repo: `git clone https://github.com/BM-N/form_extraction`
2.  Install deps: `pip install -r requirements.txt` or `poetry install`
3.  Database config: Create `.env` file (e.g., `DATABASE_URL=sqlite:///./healthcare_form_data.db`).
4.  Run API: `uvicorn app.main:app --reload` (http://127.0.0.1:8000)
5.  Run Streamlit: `streamlit run streamlit_app.py` (http://localhost:8501)

### Docker Setup

1.  Clone repo: `git clone https://github.com/BM-N/form_extraction`
2.  Build image: `docker build -t healthcare-form-app .`
3.  Run container: `docker run -p 8501:8501 -p 8000:8000 healthcare-form-app`
    *   Streamlit: http://localhost:8501
    *   API: http://localhost:8000

## Usage

1.  Access Streamlit UI (http://localhost:8501).
2.  Upload form image.
3.  Application processes image, extracts data, displays output, and stores in DB.
4.  Review data in UI or database.
5.  API docs at http://localhost:8000/docs.

## Contributing

Feel free to fork, branch, commit changes, and submit pull requests.

## License

MIT License.
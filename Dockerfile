FROM python:3.11.9

WORKDIR /main_image_app/

COPY ./requirements.txt /main_image_app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /main_image_app/requirements.txt

COPY ./src /main_image_app/src

COPY ./fe /main_image_app/fe

EXPOSE 8000
EXPOSE 8501

CMD ["sh","-c","fastapi run src/main.py --port 8000 & streamlit run fe/web_app.py"]
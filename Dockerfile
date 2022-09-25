FROM python:3.7-slim

RUN pip install flask

RUN pip install flask-mysql

RUN pip install flask_cors

RUN mkdir templates

RUN mkdir static

COPY app.py /app.py

COPY view/*  /view/

RUN chmod -R a+rwx templates

CMD ["python","app.py"]
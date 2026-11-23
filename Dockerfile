FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY templates/ templates/
COPY students.xlsx .


EXPOSE 5000

CMD ["python","app.py"]


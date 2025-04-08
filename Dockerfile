FROM python:3.13.2-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python translate.py

EXPOSE 8050

CMD ["python", "main.py"]
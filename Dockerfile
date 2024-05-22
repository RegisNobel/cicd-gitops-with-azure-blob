FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

#ARG AZURE_CONNECTION_STRING
#ENV AZURE_CONNECTION_STRING=${AZURE_CONNECTION_STRING}

CMD ["python3", "app.py"]

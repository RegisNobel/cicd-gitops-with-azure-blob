FROM python:3.11-slim

# Set the working directory
WORKDIR /usr/src/app

# Define ARG and ENV in sequence
#ARG AZURE_CONNECTION_STRING
#ENV AZURE_CONNECTION_STRING=${AZURE_CONNECTION_STRING}

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Expose the port your app runs on
EXPOSE 5002

# Set the default command
ENTRYPOINT ["python3"]
CMD ["app.py"]

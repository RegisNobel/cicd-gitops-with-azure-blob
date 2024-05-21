import os
from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()  # This loads the environment variables from .env

# Azure storage details
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
CONTAINER_NAME = "ytdlblob"

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.first()

        # Download the video locally
        local_filename = stream.default_filename
        stream.download(filename=local_filename)

        try:
    # Upload the file to Azure Blob Storage
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=local_filename)
            with open(local_filename, "rb") as data:
                blob_client.upload_blob(data)
                print("Upload successful.")
        except Exception as e:
            print("An error occurred:", e)


        # Remove the local file after uploading
        os.remove(local_filename)

        return redirect(url_for('success', link=url))
    return render_template('index.html')


@app.route('/success')
def success():
    link = request.args.get('link')
    return render_template('success.html', link=link)


if __name__ == "__main__":
    app.run(debug=True)

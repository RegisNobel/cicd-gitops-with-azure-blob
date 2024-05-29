import os
from flask import Flask, render_template, request, redirect, url_for, flash
from pytube import YouTube
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

load_dotenv()  # This loads the environment variables from .env

# Azure storage details
azConnectionString = os.getenv('azConnectionString')
CONTAINER_NAME = "ytdlblob"
AZURE_STORAGE_ACCOUNT_NAME = "ytdlstoredemo"

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(azConnectionString)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            stream = yt.streams.first()
        except AttributeError as e:
            flash(f"Failed to process YouTube URL: {e}")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"An error occurred: {e}")
            return redirect(url_for('index'))

        # Download the video locally
        local_filename = stream.default_filename
        try:
            stream.download(filename=local_filename)
        except Exception as e:
            flash(f"Failed to download the video: {e}")
            return redirect(url_for('index'))

        try:
            # Upload the file to Azure Blob Storage
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=local_filename)
            with open(local_filename, "rb") as data:
                blob_client.upload_blob(data)
                print("Upload successful.")
        except Exception as e:
            flash(f"Failed to upload the video to Azure Blob Storage: {e}")
            return redirect(url_for('index'))

        # Remove the local file after uploading
        os.remove(local_filename)

        return redirect(url_for('success', link=url, filename=local_filename))
    return render_template('index.html')


@app.route('/success')
def success():
    link = request.args.get('link')
    local_filename = request.args.get('filename')
    blob_url = f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{local_filename}"
    return render_template('success.html', link=link, blob_url=blob_url)


if __name__ == "__main__":
    app.run(debug=True, port=5002, host="0.0.0.0")

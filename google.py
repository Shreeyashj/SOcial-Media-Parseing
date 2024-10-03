import streamlit as st
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ----------------------------
# Configuration
# ----------------------------
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'  # Update with your service account file path

# ----------------------------
# Function to authenticate and fetch Google Drive files
# ----------------------------
def authenticate_and_fetch_files():
    # Authenticate using service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Create the Drive API client
    service = build('drive', 'v3', credentials=credentials)

    # Fetch files
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])
    
    return items

# ----------------------------
# Streamlit App
# ----------------------------
st.title("My Google Drive Files")

if st.button("Fetch Google Drive Files"):
    try:
        files = authenticate_and_fetch_files()
        if not files:
            st.write("No files found.")
        else:
            st.write("Files:")
            for file in files:
                st.write(f"Name: {file['name']}, ID: {file['id']}, Type: {file['mimeType']}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Run the app
if __name__ == '__main__':
    st.run()

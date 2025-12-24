from oryks_google_drive import GoogleDrive
from oryks_google_drive.mime_types import MimeType
import json

def save_resource(resource: dict, resource_name: str) -> None:
    resource_name = f'{resource_name}.json'
    with open(resource_name, 'w') as f:
        json.dump(resource, fp=f, indent=4)


def load_resource(resource_path: str) -> dict:
    with open(resource_path, 'r') as f:
        return json.load(f)


client_secrets_file = '/home/lyle/Downloads/secret.json'
drive = GoogleDrive()
# drive.authenticate(client_secret_file=client_secrets_file)
drive.authenticate_from_credentials(
    credentials_path='/home/lyle/.drive/credentials.json'
)
# Example usage
# for file in drive.list_files():
#     print(f"File ID: {file['id']}, Name: {file['name']}")
# file_id = 'your_file_id_here'
# file_content = drive.download_file(file_id)
# print(f"Downloaded file content: {file_content[:100]}...")  # Print the first 100 characters
# audio_path = '/home/lyle/datasets/audio/maongezi/raw/maongezi_001.wav'
# mime_type = MimeType.AUDIO_WAV.value
# f = drive.upload_file(file_path=audio_path, mime_type=mime_type)
# print(f)
file_id = '1alI9X1YZRa2XY6eBMOMXWbOYXTiEPrxg'
# file_metadata = drive.get_file_metadata(file_id)
# print(file_metadata)
# save_resource(file_metadata, 'file_metadata')
# permissions = [{
#     'type': 'anyone',
#     'role': 'reader'
# }]
# resp = drive.update_file_permissions(file_id, permissions)
# print(resp)
# file_path = 'audio_downloaded.wav'
# success = drive.download_file(file_id, file_path)
# print(f"File downloaded successfully: {success}")
# folder_name = 'Test Upload Folder'
# folder = drive.create_folder(folder_name)
# print(folder)
# folder_id = '176sZiyVaHQlIeZvLZVO3Wy3IJvxN-vqe'
# resp = drive.move_file(file_id, folder_id)
# print(resp)
# for folder in drive.list_folders():
#     print(f"Folder ID: {folder['id']}, Name: {folder['name']}")
folder_id: str = "1jYlksmN4vIcNkBuSoPrUfvZAQ9iO5fnA"
for file in drive.list_files_in_folder(folder_id):
    print(f"File ID: {file['id']}, Name: {file['name']}")

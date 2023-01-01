from google.oauth2.credentials import Credentials

from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(video_path, channel_id):
    # Load the credentials from the environment variables
    credentials = Credentials.from_authorized_user_info()

    youtube = build('youtube', 'v3', credentials=credentials)

    # Set the metadata for the video
    video_metadata = {
        'snippet': {
            'categoryId': '22',
            'channelId': channel_id,
            'description': 'A video uploaded using the YouTube API',
            'title': 'YouTube API Video'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    # Set the path to the video file
    media = MediaFileUpload(video_path,
                            mimetype='video/*',
                            chunksize=1024*1024,
                            resumable=True)

    # Call the YouTube API to upload the video
    response = youtube.videos().insert(
        part='snippet,status',
        body=video_metadata,
        media_body=media
    ).execute()

    print(f'Video uploaded: {response["id"]}')

def main():
    video_path = '/path/to/video.mp4'
    channel_id = 'UCCHANNEID'
    upload_video(video_path, channel_id)

if __name__ == '__main__':
    main()

# this is just an example for me to learn about the youtube api and use the api key

from googleapiclient.discovery import build

# Set up the YouTube API service
youtube = build('youtube', 'v3', developerKey='AIzaSyCa3wqdNV5o3wrWX_QkNEWRr1l1Xk8GjII')

# Example: Search for videos related to 'machine learning'
search_response = youtube.search().list(
    q='machine learning',
    part='snippet',
    type='video',
    maxResults=10
).execute()

# Print the titles of the returned videos
for item in search_response['items']:
    print(item['snippet']['title'])

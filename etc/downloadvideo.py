from pytube import YouTube

# Function to download YouTube video given a link
def download_youtube_video(link):
    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download()

        print(f"Download complete: {yt.title}")
    except Exception as e:
        print(f"Error downloading {link}: {str(e)}")

# Read YouTube links from the file
file_path = "youtube_links.txt"

with open(file_path, "r") as file:
    youtube_links = file.readlines()

# Download each video
for link in youtube_links:
    link = link.strip()  # Remove leading/trailing whitespaces
    download_youtube_video(link)

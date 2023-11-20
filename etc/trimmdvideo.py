from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def trim_videos(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp4"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            with VideoFileClip(input_path) as video:
                trimmed_video = video.subclip(4, video.duration - 3)
                trimmed_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_folder = input("Enter the path of the folder containing .mp4 files: ")

    output_folder = input("Enter the path of the folder to save trimmed videos: ")

    trim_videos(input_folder, output_folder)

    print("Videos trimmed and saved successfully!")

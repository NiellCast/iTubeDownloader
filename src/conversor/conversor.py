from moviepy.editor import *


class Conversor:
    @staticmethod
    def converter(video_path: str, audio_path: str) -> None:
        video = VideoFileClip(video_path)
        audio = video.audio

        with video:
            with audio:
                audio.write_audiofile(audio_path)

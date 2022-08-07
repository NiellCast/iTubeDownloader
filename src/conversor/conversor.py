from moviepy.editor import *


class Conversor:
    @staticmethod
    def converter(video_path: str, audio_path: str) -> None:
        """
        :param video_path: Recebe o caminho do vídeo baixado.
        :param audio_path: Recebe o caminho para onde o arquivo mp3 será salvo.
        :return: Converte o vídeo mp4 em áudio mp3.
        """

        video = VideoFileClip(video_path)
        audio = video.audio

        with video:
            with audio:
                audio.write_audiofile(audio_path)

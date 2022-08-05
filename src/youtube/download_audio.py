from pytube import YouTube, Playlist


class Downloader:
    @staticmethod
    def regular_download(url: str) -> None:
        video = YouTube(url)
        video.streams.filter(only_audio=True)
        video.streams.get_audio_only().download(output_path=r'downloads')

from pytube import YouTube


class Downloader:
    @staticmethod
    def regular_download(url: str) -> None:
        video = YouTube(url)
        video.streams.get_lowest_resolution().download(output_path=r'downloaded')

    @staticmethod
    def get_name(url) -> str:
        return YouTube(url).title.replace('.', '')

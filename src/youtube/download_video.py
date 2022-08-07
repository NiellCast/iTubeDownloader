from pytube import YouTube


class Downloader:
    @staticmethod
    def regular_download(url: str) -> None:
        """
        :param url: Recebe a url do vídeo a ser baixado.
        :return: Faz o download do vídeo recebido pelo Telegram.
        """

        video = YouTube(url)
        video.streams.get_lowest_resolution().download(output_path=r'downloaded')

    @staticmethod
    def get_name(url: str) -> str:
        """
        :param url: Recebe a url do vídeo a ser baixado.
        :return: Retorna o nome do vídeo.
        """

        return YouTube(url).title.replace('.', '')

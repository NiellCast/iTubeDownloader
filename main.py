from time import sleep
from src.telegram.bot import Bot
from src.telegram.links import CleanLink
from src.youtube.download_audio import Downloader
import pytube.exceptions
from src.conversor.conversor import Conversor
from src.delete.delete_file import Delete


def run() -> None:
    bot = Bot()

    @bot.message_handler(commands=['start', 'help'])
    def get_started(message) -> None:
        """
        :param message: Recebe /start e /help do usuário.
        :return: Envia mensagens de ajuda para o usuário.
        """

        mensagens = ['Envie o comando /baixar + o link do seu vídeo para fazer o download!',
                     'Exemplo: /baixar https://www.youtube.com/watch?v=z2Dn0MeWCws&list=RDR77IDMm5D2Y&index=2']

        for m in mensagens:
            bot.reply_to(message, m)

    @bot.message_handler(commands=['baixar'])
    def get_video_link(message) -> None:
        """
        :param message: Recebe /baixar + Youtube link do usuário para iniciar a interação.
        :return: Envia para o usuário o áudio em .mp3 do vídeo requerido.
        """

        bot.reply_to(message, f'Olá, {message.from_user.first_name}! Seu áudio ficará pronto em breve!')
        sleep(3)

        link = CleanLink.clear_link(message.text)

        try:
            Downloader.regular_download(link)
            song_name = Downloader.get_name(link)
            sleep(5)

            video_path = f'downloaded/{song_name}.mp4'
            audio_path = video_path.replace('.mp4', '.mp3')

            # print(song_name)
            # print(os.listdir('downloaded'))

            Conversor.converter(video_path, audio_path)
            bot.send_audio(message.chat.id, open(audio_path, 'rb'))

            Delete.deletar([video_path, audio_path])

        except pytube.exceptions.VideoUnavailable:
            bot.reply_to(message, 'Infelizmente não foi possível fazer o download deste vídeo :(')
        except pytube.exceptions.RegexMatchError:
            bot.reply_to(message, 'Não encontrei nenhum vídeo com este endereço :(')

    bot.polling()


if __name__ == '__main__':
    run()

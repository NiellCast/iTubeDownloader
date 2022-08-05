from time import sleep
from src.telegram.bot import Bot
from src.telegram.links import CleanLink
from src.youtube.download_audio import Downloader
import pytube.exceptions


def run() -> None:
    bot = Bot()

    @bot.message_handler(commands=['start', 'help'])
    def get_started(message) -> None:
        mensagens = ['Envie o comando /baixar + o link do seu vídeo para fazer o download!',
                     'Exemplo: /baixar https://www.youtube.com/watch?v=z2Dn0MeWCws&list=RDR77IDMm5D2Y&index=2']

        for m in mensagens:
            bot.reply_to(message, m)

    @bot.message_handler(commands=['baixar'])
    def get_video_link(message) -> None:
        bot.reply_to(message, f'Olá, {message.from_user.first_name}! Seu áudio ficará pronto em breve!')
        sleep(3)

        try:
            Downloader.regular_download(CleanLink.clear_link(message.text))
        except pytube.exceptions.VideoUnavailable:
            bot.reply_to(message, 'Infelizmente não foi possível fazer o download deste vídeo :(')
        except pytube.exceptions.RegexMatchError:
            bot.reply_to(message, 'Não encontrei nenhum vídeo com este endereço :(')

    bot.polling()


if __name__ == '__main__':
    run()

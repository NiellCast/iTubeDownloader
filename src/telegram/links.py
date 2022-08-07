class CleanLink:
    @staticmethod
    def clear_link(msg: str) -> str:
        """
        :param msg: Recebe a mensagem bruta enviada pelo usuário.
        :return: Retorna somente o link do vídeo sem o comando "/baixar".
        """

        msg = msg.replace(' ', '')[7:]
        return msg

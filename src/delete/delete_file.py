import os
from typing import List


class Delete:
    @staticmethod
    def deletar(file: List) -> None:
        """
        :param file: Recebe o nome dos arquivos baixados.
        :return: Deleta os arquivos que já foram enviados para o usuário e já não são úteis.
        """

        for f in file:
            os.remove(f)


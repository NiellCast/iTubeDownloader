import os
from typing import List


class Delete:
    @staticmethod
    def deletar(files: List) -> None:
        """
        :param files: Recebe o nome dos arquivos baixados.
        :return: Deleta os arquivos que já foram enviados para o usuário e já não são úteis.
        """

        for file in files:
            os.remove(file)


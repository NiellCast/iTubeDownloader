import os
from typing import List


class Delete:
    @staticmethod
    def deletar(file: List) -> None:
        for f in file:
            os.remove(f)


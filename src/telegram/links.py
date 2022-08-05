class CleanLink:
    @staticmethod
    def clear_link(msg: str) -> str:
        msg = msg.replace(' ', '')[7:]
        return msg

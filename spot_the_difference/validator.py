import re
class GameValid:
    @staticmethod
    def validate(string):
        pattern = re.compile(r"[A-Z][1-9]+")

        return pattern.match(string).group()
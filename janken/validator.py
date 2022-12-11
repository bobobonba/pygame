class JankenValid:
    def __init__(self, choices):
        self.choices = choices
    
    def validate(self, string):
        result = string in self.choices
        if result is False:
            return False
        else:
            return string
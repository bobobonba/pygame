class Validator:
    def validate(string, correct_choice):
        to_s = lambda var : str(var)

        if string in list(map(to_s, correct_choice)):
            return string
        else:
            return False
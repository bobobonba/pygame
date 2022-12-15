class Display:
    def first_line(list):
        template = '| ____ |'
        string = '|' + '|'.join(list) + '|'

        return template + string

    def show_table(bet_table, dict_in_list):
        for attr in bet_table:
            string = ''
            template = None
            if type(attr) is str:
                template = f'| {attr}(x8)|'
            else:
                template = f'| {attr}(x2)|'
            
            string += template

            for dict in dict_in_list:
                if attr in dict:
                    string += f'|{dict[attr]}'
                else:
                    string += f'|00'

            print(string)
        


                


import re
# создаем словарь для части токенов и  их регулярок
tokens_dict = {

    'if' : r'trigger',
    'var_declare' : r'var',
    'output' : r'console',
    'input' : r'entry',
    'var_ident' : r'[a-zA-Z]+',
    # 'operator' : r'[+-=/*]',
    'digit' : r'\d+',
    'log_operator' : r'[<>!=&|]',
    'start_func' : r'{',
    'end_func' : r'}',
    'void_line' : r'\n'
}
# класс лексера
class Lexer(object):
    # создание переменной в которой хранится текст при создании класса
    def __init__(self, content):
        self.content = content
    # функйия для токенизации
    def tokenize(self, error):
        # создаем список слов

        if self.content[-1] in '{};':
            words_to_tokenize = self.content.split()
            # стартовый индекс списка и сисок с токенами
            cur_index = 0
            tokens = []
            # цикл для перебора всех слов в списке
            while cur_index < len(words_to_tokenize):
                # конкретное слово из списка
                word = words_to_tokenize[cur_index]
                # цикл для перебора регулярок и определение токена и его значения
                for r_comp in tokens_dict.keys():

                    if re.search(tokens_dict[r_comp], word):
                        if word[-1] == ';':
                            word = word[:-1]
                            tokens.append([r_comp, word])
                            tokens.append(['end_line', ';'])
                        else:
                            tokens.append([r_comp, word])
                        break
                    elif word in '+-*/':
                        tokens.append(['operator', word])
                        break
                    elif word == '=':
                        tokens.append(['assignment', word])
                        break

                cur_index += 1
            # возвращаем список токенов

            return tokens

        elif self.content == None:
            pass
        else:
            print(f'Отсутствует ; в конце строки {error}')
            quit()
            return tokens


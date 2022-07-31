import os
from System.Lexer import *
from System.Parser import *
from System.Memory import *

class Compiler(object):

    def __init__(self, filename):
        self.compile(filename)

    def compile(self, filename):
        if os.path.splitext(filename)[-1] == '.fir':
            if os.path.exists(filename):
                memory = Memory()
                with open(filename, 'r') as f:
                    error = 0
                    for line in f:
                        error += 1
                        if line != '\n':
                            lex = Lexer(line.strip('\n'))
                            tokens = lex.tokenize(error)
                            # print(tokens)
                            parser = Parser(memory, error)
                            parser.parse(tokens)

            else:
                print(f'Нет файла {filename} в дериктории или указан неполный путь')
                quit()
        else:
            print(f'Язык Пихта не имеет расширения {os.path.splitext(filename)[-1]}')
            quit()

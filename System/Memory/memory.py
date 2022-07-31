class Memory(object):

    def __init__(self):
        self.save_vars = {}
        self.condition = None
        self.true_condition = None
        self.false_condition = None
        self.if_was = False
        self.start = False

    def save(self, variable, value):
        self.save_vars[variable] = value

    def save_condition(self, condition):
        self.condition = eval(condition)

    def append_true_commands(self, tokens):
        self.true_condition.append(tokens)

    def if_save(self, bool):
        self.if_was = bool

    def save_start(self, bool):
        self.start = bool

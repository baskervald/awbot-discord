from random import randint

class Expression:
    def __init__(self, string, mult=1):
        self.tree = []
        self.expr = string
        self.mult = mult
        self.failed = False
        if '+' in string:
            self.complex = True
            print(string + ' is complex')
        else:
            self.complex = False
            print(string + ' is simple')

    def evaluate(self):
        if self.complex:
            self.eval_complex(self.expr)
        else:
            self.eval_simple(self.expr)

    def eval_complex(self, string):
        buf = ''
        wait = 0
        mult = 1
        for c in string:
            if wait == 0 and c is '+':
                if buf == '':
                    self.failed = True
                    return False
                else:
                    self.tree.append(Expression(buf, mult=mult))
                    buf = ''
                    mult = 1
            elif c is ')':
                if wait > 0:
                    wait = wait - 1
                else:
                    self.failed = True
                    return False
            elif c is '(':
                wait = wait + 1
                if buf.isdigit() and wait == 1:
                    mult = int(buf)
                    buf = ''
                elif buf != '':
                    self.failed = True
                    return False
            elif c is not ' ':
                buf += c
        if wait is not 0:
            self.failed = True
            return False
        self.tree.append(Expression(buf, mult=mult))
        self.value = 0
        if self.mult is not 1:
            self.string = str(self.mult) + '('
        else:
            self.string = '('
        for expr in self.tree:
            expr.evaluate()
            if expr.failed:
                self.failed = True
                return False
            self.value = self.value + expr.value
            self.string = self.string + expr.string + "+"
        self.value = self.value * self.mult
        self.string = self.string[:-1] + ')'

    def eval_simple(self, string):
        if string.isdigit():
            self.value = int(string)
            self.string = string
        elif string.count('d') == 1:
            split = string.split('d')
            if split[0] == '':
                split[0] = 1
            self.string = '[' + string + ']('
            self.value = 0
            for _ in range(int(split[0])):
                val = randint(1, int(split[1])+1)
                self.string = self.string + str(val) + '+'
                self.value = self.value + val
            self.string = self.string[:-1] + ')'
        else:
            self.failed = True
            return False

def roll(string):
    expr = Expression(string)
    expr.evaluate()
    if expr.failed:
        return "Roll failed. Please check your input and try again"
    return expr.string[1:-1] + '\n' + str(expr.value)

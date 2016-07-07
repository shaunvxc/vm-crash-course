class SimpleStack(object):

    def __init__(self):
        self.stack = []

    def dump_stack(self):
        print self.stack

    def push(self, arg):
        self.stack.append(arg)

    def pop(self):
        return self.stack.pop()

    def sum_nums(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def sumx(self):
        res = 0
        for x in range(0, self.pop()):
           res += self.pop()

        self.push(res)


class Machine1(object):
    def __init__(self):
        self.stack = SimpleStack()
        self.op_table = {
            'PUSH': lambda cmds  : self.stack.push(cmds.next()),
            'POP':  lambda cmds  : self.stack.pop(),
            'SUM':  lambda cmds  : self.stack.sum_nums(),
            'SUMX': lambda cmds  : self.stack.sumx(),
        }

    def evaluate(self, sequence):
        sequence = iter(sequence)
        while True:
            try:
                command = sequence.next()
                self.op_table[command](sequence)
            except StopIteration:
                break

    def dump_stack(self):
        self.stack.dump_stack()


if __name__ == '__main__':
    m1 = Machine1()
    m1.evaluate(['PUSH', 4, 'PUSH', 5, 'PUSH', 6, 'PUSH', 2, 'SUMX'])
    m1.dump_stack()

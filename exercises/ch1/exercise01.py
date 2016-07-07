class Machine1(object):
    def __init__(self):
        self.stack = []
        # self.stack = SimpleStack()
        self.op_table = {
            'PUSH': lambda cmds  : self.push(cmds.next()),
            'POP':  lambda cmds  : self.pop(),
            'SUM':  lambda cmds  : self.sum_nums(),
            'SUMX': lambda cmds  : self.sumx(),
        }

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def sum_nums(self):
        self.push(self.pop() + self.pop())

    def sumx(self):
        res = 0
        for x in range(0, self.pop()):
            res += self.pop()

        self.push(res)

    def evaluate(self, sequence):
        sequence = iter(sequence)
        while True:
            try:
                command = sequence.next()
                self.op_table[command](sequence)
            except StopIteration:
                break

    def dump_stack(self):
        print self.stack #self.stack.dump_stack()


if __name__ == '__main__':
    m1 = Machine1()
    m1.evaluate(['PUSH', 4, 'PUSH', 5, 'PUSH', 6, 'PUSH', 3, 'SUMX'])
    m1.dump_stack()






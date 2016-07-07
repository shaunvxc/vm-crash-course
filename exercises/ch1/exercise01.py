class Machine1(object):
    def __init__(self):
        self.stack = []
        self.op_table = {
            'PUSH': lambda cmds  : self._push(cmds.next()),
            'POP':  lambda cmds  : self._pop(),
            'SUM':  lambda cmds  : self._sum_nums(),
            'SUMX': lambda cmds  : self._sumx(),
        }

    def _push(self, value):
        self.stack.append(value)

    def _pop(self):
        return self.stack.pop()

    def _sum_nums(self):
        self._push(self._pop() + self._pop())

    def _sumx(self):
        res = 0
        for x in range(0, self._pop()):
            res += self._pop()

        self._push(res)

    def evaluate(self, sequence):
        sequence = iter(sequence)
        while True:
            try:
                command = sequence.next()
                self.op_table[command](sequence)
            except StopIteration:
                break

    def dump_stack(self):
        print self.stack


if __name__ == '__main__':
    m1 = Machine1()
    m1.evaluate(['PUSH', 4, 'PUSH', 5, 'PUSH', 6, 'PUSH', 3, 'SUMX'])
    m1.dump_stack()

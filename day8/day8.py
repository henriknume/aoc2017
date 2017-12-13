import operator

regs = {}

ex_inp = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


class Instruction:
    def __init__(self, reg, op, nr, x, cond, y):
        self.reg = reg
        self.op = self.get_op_func(op)
        self.nr = nr
        self.x = x
        self.cond = self.get_op_func(cond)
        self.y = y

    def get_op_func(self, op):
        return {
            '>' : operator.gt,
            '<' : operator.lt,
            '>=' : operator.ge,
            '<=' : operator.le,
            '==' : operator.eq,
            '!=' : operator.ne,
            'inc': operator.add,
            'dec': operator.sub
            }[op]


def parse_instructions(lines):
    regs.clear()
    inst_list = []
    for line in lines:
        arr = line.split()

        reg = arr[0]
        op = arr[1]
        nr = int(arr[2])
        # arr[3] is 'if'
        x = arr[4]
        cond = arr[5]
        y = int(arr[6])

        regs[reg] = 0
        inst_list.append(Instruction(reg, op, nr, x, cond, y))
    return inst_list


def do_inst(inst_list, is_part2):
    highest = 0
    for i in inst_list:
        if i.cond(regs[i.x], i.y):
            regs[i.reg] = i.op(regs[i.reg], i.nr)
            # part2:
            if regs[i.reg] > highest:
                highest = regs[i.reg]
    if is_part2:
        return highest
    return max(regs.values())


def main():
    inp = open('./d8.txt').read().splitlines()
    #inp = ex_inp.splitlines()

    instructions = parse_instructions(inp)
    print "Part 1: %d" % do_inst(instructions, False)

    instructions = parse_instructions(inp)
    print "Part 2: %d" % do_inst(instructions, True)


if __name__ == '__main__': main()
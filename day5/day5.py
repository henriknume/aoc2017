def do_jumps(inst_list, part2):
    instructions = map(int, inst_list)
    pc = 0
    steps = 0
    while pc < len(instructions):
        jmp_dist = instructions[pc]
        if part2 and jmp_dist >= 3:
            instructions[pc] -= 1
        else:
            instructions[pc] += 1
        pc += jmp_dist
        steps += 1
    return steps


def main():
    inp = open("./d5.txt").read().splitlines()
    print "T1: %d" % do_jumps(['0', '3', '0', '1', '-3'], False)
    print "Part 1: %d" % do_jumps(inp, False)
    print "T2: %d" % do_jumps(['0', '3', '0', '1', '-3'], True)
    print "Part 2: %d" % do_jumps(inp, True)


if __name__ == "__main__": main()

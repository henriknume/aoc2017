
def captcha(seq, part2):
    L = len(seq)
    offset = L/2 if part2 else 1
    sum = 0
    for i in range(L):
        if int(seq[i]) == int(seq[(i + offset) % L]):
            sum += int(seq[i])
    return sum

def main():
    inp = open("inputs/d1.txt").read()
    print "Part 1: %d" % captcha(inp, False)
    print "Part 2: %d" % captcha(inp, True)


if __name__ == "__main__": main()
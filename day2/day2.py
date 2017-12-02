def checksum(inp):
    rows = inp.splitlines()
    s = 0
    for r in rows:
        numbers = map(int, r.split())
        s += max(numbers) - min(numbers)
    return s


def divs(inp):
    rows = inp.splitlines()
    s = 0
    for r in rows:
        numbers = map(int, r.split())
        for n in numbers:
            for d in numbers:
                if (n % d) == 0 and n != d:
                    s += (n / d)
    return s


def main():
    inp = open("./d2.txt").read()
    print "Part 1: %d" % checksum(inp)
    print "Part 2: %d" % divs(inp)


if __name__ == "__main__": main()
class Memory:
    def __init__(self, mem_state):
        self.memory = mem_state
        self.prev_states = {}
        self.loop_size = -1

    def re_alloc(self):
        count = 0
        while True:
            self.save_state()
            self.re_dist()
            count += 1
            if self.seen_before():
                break
        return count

    def re_dist(self):
        hi = self.get_max_blocks_index()
        popped_val = self.memory[hi]
        self.memory[hi] = 0
        for i in range(1, popped_val + 1):
            self.memory[(hi + i) % len(self.memory)] += 1

    def seen_before(self):
        for key in self.prev_states:
            value = self.prev_states[key]
            if value == self.memory:
                self.loop_size = len(self.prev_states) - key
                return True
        return False

    def save_state(self):
        size = len(self.prev_states)
        self.prev_states[size] = self.memory[:]

    def get_max_blocks_index(self):
        highest = 0
        for i in range(0, len(self.memory)):
            curr = self.memory[i]
            if curr > self.memory[highest]:
                highest = i
        return highest

    def print_prev(self):
        print "prev_states:"
        print ">%s" % self.prev_states


def main():
    inp = map(int, open('./d6.txt').read().split())
    m = Memory(inp)
    print "Part 1: %d" % m.re_alloc()
    print "Part 2: %d" % m.loop_size

if __name__ == '__main__': main()

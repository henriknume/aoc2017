matrix = {}


def walk(n):
    dirs = ['R', 'U', 'L', 'D']
    curr_dir = 0
    dx = 0
    dy = 0
    tot_steps = 1
    walk_length = 1
    while tot_steps < n:
        i = 0
        while i < walk_length and tot_steps < n:
            direction = dirs[curr_dir % len(dirs)]
            if direction == 'R':
                dx += 1
            elif direction == 'U':
                dy += 1
            elif direction == 'L':
                dx -= 1
            elif direction == 'D':
                dy -= 1
            tot_steps += 1
            i += 1
        curr_dir += 1
        if curr_dir % 2 == 0:
            walk_length += 1
    return abs(dx) + abs(dy)


def walk_with_values(n):
    matrix.clear()
    matrix['0x0'] = 1
    dirs = ['R', 'U', 'L', 'D']
    curr_dir = 0
    dx = 0
    dy = 0
    tot_steps = 1
    walk_length = 1
    while tot_steps < n:
        i = 0
        while i < walk_length and tot_steps < n:
            direction = dirs[curr_dir % len(dirs)]
            if direction == 'R':
                dx += 1
            elif direction == 'U':
                dy += 1
            elif direction == 'L':
                dx -= 1
            elif direction == 'D':
                dy -= 1
            curr_sq = calc_current_sq(dx, dy)
            if curr_sq > n:
                return curr_sq
            tot_steps += 1
            i += 1
        curr_dir += 1
        if curr_dir % 2 == 0:
            walk_length += 1
    return -1


def calc_current_sq(x, y):
    # look up all surrounding coordinates and sum.
    sum_neighbours = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if not (i == 0 and j == 0):  # exclude center square
                sum_neighbours += get_value_from(x+i, y+j)
    # save in x,y
    new_key = "%dx%d" % (x, y)
    matrix[new_key] = sum_neighbours
    return sum_neighbours


def get_value_from(x, y):
    k = '%dx%d' % (x, y)
    v = 0
    if k in matrix:
        v = matrix[k]
    return v


def main():
    inp = 265149
    print "1: %s" % (walk(1) == 0)
    print "12: %s" % (walk(12) == 3)
    print "23: %s" % (walk(23) == 2)
    print "Part 1: %d" % walk(inp)
    print "Part 2: %d" % walk_with_values(inp)

if __name__ == "__main__": main()
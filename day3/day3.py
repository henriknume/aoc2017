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
    # starting top left and going around clockwise
    v1 = get_value_from(x-1, y+1)
    v2 = get_value_from(x, y+1)
    v3 = get_value_from(x+1, y+1)
    v4 = get_value_from(x+1, y)
    v5 = get_value_from(x+1, y-1)
    v6 = get_value_from(x, y-1)
    v7 = get_value_from(x-1, y-1)
    v8 = get_value_from(x-1, y)
    sum_of_neighbours = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8
    # save in x,y
    new_key = "%dx%d" % (x, y)
    matrix[new_key] = sum_of_neighbours
    return sum_of_neighbours


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
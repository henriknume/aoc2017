disks = {}


class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.parent = None
        self.children = []

    def add_parent(self, parent_node):
        self.parent = parent_node

    def add_child(self, disc):
        self.children.append(disc)

    def has_children(self):
        if len(self.children) == 0:
            return False
        return True


def parse_to_node(line):
    arr = line.split(')')
    lhs = arr[0].split()
    id = lhs[0]
    weight = int(lhs[1][1:])
    return Node(id, weight)


def parse_relation(line):
    if '->' in line:
        arr = line.split('->')
        parent_name = arr[0].split()[0]
        children = arr[1].replace(' ', '').split(',')
        for child_name in children:
            parent = disks[parent_name]
            child = disks[child_name]
            parent.add_child(child)
            child.add_parent(parent)
    return


def get_root(node):
    if node.parent is None:
        return node
    return get_root(node.parent)


def main():
    inp = open('./d7.txt').read().splitlines()
    for line in inp:
        new_disk = parse_to_node(line)
        disks[new_disk.id] = new_disk
    for line in inp:
        parse_relation(line)
    root = get_root(disks.itervalues().next())
    print "Part 1: %s" % root.id
    #print "Part 2: %d" %


if __name__ == '__main__': main()
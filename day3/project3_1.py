# We will not be generating an entire map by repeating the map to the right
# Instead, we will implement a round-map logic:
# When out of bounds to the right, circle back to the left side of the map

def get_map(filename):
    with(open(filename)) as f:
        map = f.read()
    return map.split('\n')


def solution(map):
    height = len(map)
    width = len(map[0])
    trees = 0
    x = 0
    y = 0

    while y < height - 1:
        # move toboggan
        x += 3
        y += 1
        # check if x-coordinate is over the map width, and circle around if it is
        if x >= len(map[0]):
            x = x - width
        # check if on tree
        if map[y][x] == '#':
            trees += 1

    return trees

if __name__ == '__main__':
    map = get_map('map.txt')
    print(solution(map))
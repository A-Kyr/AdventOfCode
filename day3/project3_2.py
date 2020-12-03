# We will not be generating an entire map by repeating the map to the right
# Instead, we will implement a round-map logic:
# When out of bounds to the right, circle back to the left side of the map

def get_map(filename):
    with(open(filename)) as f:
        map = f.read()
    return map.split('\n')


def solution(map, right_moves, down_moves):
    height = len(map)
    width = len(map[0])
    trees = 0
    x = 0
    y = 0

    while y < height - 1:
        # move toboggan
        x += right_moves
        y += down_moves
        # check if x-coordinate is over the map width, and circle around if it is
        if x >= len(map[0]):
            x = x - width
        # check if on tree
        if map[y][x] == '#':
            trees += 1

    return trees

if __name__ == '__main__':
    map = get_map('map.txt')
    right1 = 1
    down1 = 1
    right2 = 3
    down2 = 1
    right3 = 5
    down3 = 1
    right4 = 7
    down4 = 1
    right5 = 1
    down5 = 2

    print(solution(map, right1, down1))
    print(solution(map, right2, down2))
    print(solution(map, right3, down3))
    print(solution(map, right4, down4))
    print(solution(map, right5, down5))

    print("The product is:\n")
    print(solution(map, right1, down1)*
          solution(map, right2, down2)*
          solution(map, right3, down3)*
          solution(map, right4, down4)*
          solution(map, right5, down5))
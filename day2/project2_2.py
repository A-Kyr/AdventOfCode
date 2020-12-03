def get_data(filename):
    with(open('passwords.txt')) as f:
        data = f.read()
        # correctly split data in lines
        data = data.split('\n')

        # split each line on whitespace
        for i in range(len(data)):
            data[i] = data[i].split(' ')
            # remove semicolons
            data[i][1] = data[i][1][0:1]

        return data


def is_valid(line):
    # format the number range correctly
    positions = line[0].split('-')
    positions[0] = int(positions[0]) - 1
    positions[1] = int(positions[1]) - 1

    char = line[1]
    password = line[2]

    return (password[positions[0]] == char) != (password[positions[1]] == char)


def solution(data):
    valid_count = 0

    for line in data:
        if is_valid(line):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    data = get_data('passwords.txt')
    print(solution(data))

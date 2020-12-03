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
    range = line[0].split('-')
    char = line[1]
    password = line[2]

    count = 0
    for letter in password:
        if letter == char:
            count += 1

    return int(range[0]) <= count <= int(range[1])


def solution(data):
    valid_count = 0

    for line in data:
        if is_valid(line):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    data = get_data('passwords.txt')
    print(solution(data))

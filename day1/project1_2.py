with open('data.txt') as f:
    lines = f.read()


def sum_to_2020(number1, number2, number3):
    if number1+number2+number3 == 2020:
        return True
    return False


def solution(lines):
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            for k in range(j+1, len(lines)):
                if sum_to_2020(int(lines[i]), int(lines[j]), int(lines[k])):
                    return int(lines[i])*int(lines[j])*int(lines[k])
    return 'Nothing found'


if __name__ == '__main__':
    lines = lines.split('\n')
    print(solution(lines))


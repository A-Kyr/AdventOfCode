def get_questions(filename):
    with(open(filename)) as f:
        lines = f.readlines()

    group = ''
    questions = []

    for line in lines:
        if line == '\n':
            group = group.split('\n')
            group = group[:-1]
            questions.append(group)
            group = ''
        else:
            group = group + line
    return questions


def get_every_count(group):
    count = 0
    letters = []
    for person in group:
        for char in person:
            if all(char in person for person in group) and char not in letters:
                letters.append(char)
                count += 1
    return count


def get_total_every_count(questions):
    count = 0
    for group in questions:
        count += get_every_count(group)
    return count


def get_any_count(group):
    count = 0
    letters = []
    for person in group:
        for char in person:
            if char not in letters:
                count += 1
                letters.append(char)
    return count


def get_total_any_count(questions):
    count = 0
    for group in questions:
        count += get_any_count(group)
    return count


if __name__=='__main__':
    questions = get_questions('questions.txt')

    print(get_total_every_count(questions))
def get_seats(filename):
    with(open(filename)) as f:
        seats = f.readlines()
    return seats


"""Return a list containing the row and column"""


def decode(encoded_seat):
    # first 7 letters are for the row
    encoded_row = encoded_seat[:7]
    decoded_row = 0
    # last 3 are for the column
    encoded_column = encoded_seat[7:]
    decoded_column = 0

    for i in range(7):
        if encoded_row[i] == 'B':
            decoded_row += pow(2, (6 - i))

    for j in range(3):
        if encoded_column[j] == 'R':
            decoded_column += pow(2, (2 - j))

    return [decoded_row, decoded_column]


def seat_id(decoded_seat):
    return decoded_seat[0] * 8 + decoded_seat[1]


def make_seats():
    all_seats = []
    for i in range(128):
        for j in range(8):
            all_seats.append([i, j])

    return all_seats

if __name__ == '__main__':
    seats = get_seats('seats.txt')
    all_seats = make_seats()

    for seat in seats:
        decoded = decode(seat)
        if decoded in all_seats:
            all_seats.remove(decoded)

    print(all_seats)
    print(seat_id([85,5]))
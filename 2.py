import csv

RED = '\u001b[41m'
BLUE = "\u001b[44m"
WHITE = '\u001b[47m'
BLACK = "\u001b[40m"
END = '\u001b[0m'


def flag_cz():
    for i in range(3):
        print(BLUE + '  ' * 6 + WHITE + ' ' * 12 + RED + ' ' * 12 + END)
    for i in range(3):
        print(BLUE + '  ' * 6 + WHITE + ' ' * 12 + RED + ' ' * 12 + END)
    for i in range(3):
        print(BLUE + '  ' * 6 + WHITE + ' ' * 12 + RED + ' ' * 12 + END)


flag_cz()
print()


def uzor():
    print(BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (
        1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + END)
    print(WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (
        1) + BLACK + '  ' * (1) + WHITE + '  ' * (1)
          + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (
              1) + WHITE + '  ' * (1) + END)
    print(WHITE + '  ' * (2) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (
        3) + BLACK + '  ' * (
              1) + WHITE + '  ' * (2) + END)
    print(WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (
        1) + BLACK + '  ' * (1) + WHITE + '  ' * (1)
          + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (
              1) + WHITE + '  ' * (1) + END)
    print(BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (
        1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + END)


uzor()
print()


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (9-i)
            if i == 9:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for j in range(10):
            if abs(array_fi[i][0] - res[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(array_pl[i][j]) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0  1 2 3 4 5 6 7 8 9' + END)


array_pl = [[0 for h in range(10)] for row in range(10)]
result = [0 for h in range(10)]

for i in range(10):
    result[i] = i ** 2

step = round(abs(result[9] - result[0]) / 9, 1)

array_init(array_pl, step)
array_fill(array_pl, result, step)
draw_plot(array_pl)
print()

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    big = 0
    small = 0
    z = -1
    for row in list(books)[1:]:
        year = row[6][:4]

        if int(year) <= 2014:
            small += 1
        else:
            big += 1

all = big + small

a = small * 100 // all
b = big * 100 // all + 1

print("До 2014    " + BLUE + '  ' * a + END + ' ' + str(a) + '%')
print()
print("После 2014 " + BLUE + '  ' * b + END + ' ' + str(b) + '%')
print()
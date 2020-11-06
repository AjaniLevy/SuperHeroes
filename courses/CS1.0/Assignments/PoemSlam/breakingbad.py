from random import randint
from random import choices
from random import shuffle
def get_file_lines(filename):
    with open(filename, "r") as INSIDE:
        filings = INSIDE.readlines()
    return filings

def lines_printed_backwards(LISTOLINES):
    LISTOLINES.reverse()
    lines_list = (len(LISTOLINES))
    for i in range(lines_list):
        line = LISTOLINES[i]
        line_num = lines_list + i
        print(f"{line_num} {line}")

POEMLIST = get_file_lines("poem.txt")


def lines_printed_random(LISTOLINES):
    shuffle(LISTOLINES)
    lines_list = (len(LISTOLINES))
    for i in range(lines_list):
        line = LISTOLINES[i]
        line_num = lines_list - i
        print(f"{line_num} {line}")

def lines_printed_FRACTAL(LISTOLINES):
   RANDOMSQUARED = choices(LISTOLINES, k = (randint((len(LISTOLINES)), 100)))
   for i in range(len(RANDOMSQUARED)):
       line = RANDOMSQUARED[i]
       print(f"{line}")


lines_printed_FRACTAL(POEMLIST)



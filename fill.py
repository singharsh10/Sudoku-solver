import pyautogui as pg
import time

sudoku = []

for i in range(9):
    row = list(input( f"Enter row {i}:  "))
    tmp = []
    for val in row:
        tmp.append(int(val))

    sudoku.append(tmp)

time.sleep(2)


def valid_number(sud, row, column, num):

    for i in range(9):
        if i != row and sud[i][column] == num:
            return False

    for j in range(9):
        if j != column and sud[row][j] == num:
            return False

    box_i = int(row / 3)
    box_j = int(column / 3)

    for i in range( 3*box_i, 3*(box_i + 1) ):
        for j in range( 3*box_j, 3*(box_j + 1) ):
            if i == row and j == column:
                continue
            if sud[i][j] == num:
                return False

    return True


def find_empty(sud):

    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                return [i, j]

    return []


def solve(sud):

    while 1:
        position = find_empty(sud)

        if position != []:
            row = position[0]
            column = position[1]

            for num in range(1, 10):
                if valid_number(sud, row, column, num):
                    sud[row][column] = num
                    if not solve(sud):
                        sud[row][column] = 0

            if sud[row][column] == 0:
                return False

        else:
            return True


solve(sudoku)

for i in range(9):
    for j in range(9):
        pg.press(str(sudoku[i][j]))
        pg.press('right')

    pg.press('down')
    for j in range(9):
        pg.press('left')

import pygame
import copy
import time

# import SolveSudoku

pygame.init()

# sudoku
sudoku = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]
duplicate = copy.deepcopy(sudoku)

# window Setup
win = pygame.display.set_mode((450, 520))
pygame.display.set_caption("Sudoku")
icon = pygame.image.load("sudoku.png")
pygame.display.set_icon(icon)

# run status
run = True

# click status
select = False
txt = ""

# font
font = pygame.font.Font('freesansbold.ttf', 32)

# wrong answer
wrongnumber = 4

#time
timestart= time.time()


# solve sudoku
def solveSudoku(grid):
    l = complete(grid)
    if l == True:
        return True
    row, column = map(int, l)
    for res in range(1, 10):
        if safe(grid, row, column, res):
            grid[row][column] = res
            win.fill((0, 0, 0))
            gridmaker()
            printboard(grid)
            drawgreenbox(column, row)
            pygame.display.update()
            pygame.time.delay(100)
            # print("ok")
            if solveSudoku(grid):
                return True
            grid[row][column] = 0
            win.fill((0, 0, 0))
            gridmaker()
            printboard(grid)
            drawredbox(column, row)
            pygame.display.update()
            pygame.time.delay(100)
            # print("ok2")
    return False


def complete(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return ((i, j))
    return True


def checksg(grid, row, column, res):
    # first SubGrid
    if row <= 2 and column <= 2:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == res:
                    return False
        return True
    # second SubGrid
    elif row <= 2 and column > 2 and column <= 5:
        for i in range(3):
            for j in range(3, 6):
                if grid[i][j] == res:
                    return False
        return True
    # Third SubGrid
    elif row <= 2 and column > 5 and column <= 8:
        for i in range(3):
            for j in range(6, 9):
                if grid[i][j] == res:
                    return False
        return True
    # Fourth SubGrid
    elif row > 2 and row <= 5 and column <= 2:
        for i in range(3, 6):
            for j in range(3):
                if grid[i][j] == res:
                    return False
        return True
    # Fifth SubGrid
    elif row > 2 and row <= 5 and column > 2 and column <= 5:
        for i in range(3, 6):
            for j in range(3, 6):
                if grid[i][j] == res:
                    return False
        return True
        # sixth SubGrid
    elif row > 2 and row <= 5 and column > 5 and column <= 8:
        for i in range(3, 6):
            for j in range(6, 9):
                if grid[i][j] == res:
                    return False
        return True
    # Seventh Subgrid
    elif row > 5 and row <= 8 and column <= 2:
        for i in range(6, 9):
            for j in range(3):
                if grid[i][j] == res:
                    return False
        return True
    # Eighth SubGrid
    elif row > 5 and row <= 8 and column > 2 and column <= 5:
        for i in range(6, 9):
            for j in range(3, 6):
                if grid[i][j] == res:
                    return False
        return True
    # Ninth SubGrid
    else:
        for i in range(6, 9):
            for j in range(6, 9):
                if grid[i][j] == res:
                    return False
        return True


def safe(grid, row, column, res):
    for x in range(9):
        if grid[row][x] == res:
            a = False
            break
    else:
        a = True
    for y in range(9):
        if grid[y][column] == res:
            b = False
            break
    else:
        b = True
    c = checksg(grid, row, column, res)
    if a == True and b == True and c == True:
        return True
    else:
        return False


def drawredbox(x, y):
    box = pygame.draw.rect(win, (255, 0, 0), (x * 50 + 1, y * 50 + 1, 49, 49), 4)


def drawgreenbox(x, y):
    box = pygame.draw.rect(win, (0, 255, 0), (x * 50 + 1, y * 50 + 1, 49, 49), 4)


# print sudoku on board
def printboard(sudoku1):
    for i in range(9):
        for j in range(9):
            if sudoku1[i][j] != 0:
                text = font.render(str(sudoku1[i][j]), True, (255, 255, 255))
                win.blit(text, ((j * 50) + 17, (i * 50) + 10))


def updateboard(sudoku1, duplicate1, pos1, txt1):
    if pos1[0] < 450 and pos1[1] < 450:
        column = pos1[0] // 50
        row = pos1[1] // 50
        if sudoku1[row][column] == 0:
            duplicate1[row][column] = txt1


# check number on board
def checksubgrid(duplicate1, row, column, res):
    # first SubGrid
    if row <= 2 and column <= 2:
        for i in range(3):
            for j in range(3):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # second SubGrid
    elif row <= 2 and column > 2 and column <= 5:
        for i in range(3):
            for j in range(3, 6):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Third SubGrid
    elif row <= 2 and column > 5 and column <= 8:
        for i in range(3):
            for j in range(6, 9):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Fourth SubGrid
    elif row > 2 and row <= 5 and column <= 2:
        for i in range(3, 6):
            for j in range(3):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Fifth SubGrid
    elif row > 2 and row <= 5 and column > 2 and column <= 5:
        for i in range(3, 6):
            for j in range(3, 6):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # sixth SubGrid
    elif row > 2 and row <= 5 and column > 5 and column <= 8:
        for i in range(3, 6):
            for j in range(6, 9):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Seventh Subgrid
    elif row > 5 and row <= 8 and column <= 2:
        for i in range(6, 9):
            for j in range(3):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Eighth SubGrid
    elif row > 5 and row <= 8 and column > 2 and column <= 5:
        for i in range(6, 9):
            for j in range(3, 6):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True
    # Ninth SubGrid
    else:
        for i in range(6, 9):
            for j in range(6, 9):
                if duplicate1[i][j] == res and (row, column) != (i, j):
                    return False
        return True


def checknum(duplicate1, pos1, txt1):
    column = pos1[0] // 50
    row = pos1[1] // 50
    for x in range(9):
        if duplicate1[row][x] == txt1 and x != column:
            a = False
            break
    else:
        a = True
    for y in range(9):
        if duplicate1[y][column] == txt1 and y != row:
            b = False
            break
    else:
        b = True
    c = checksubgrid(duplicate1, row, column, txt1)
    if a == True and b == True and c == True:
        return True
    else:
        return False


# grid
def gridmaker():
    i = 0
    for l in range(0, 10):
        if l % 3 == 0:
            pygame.draw.line(win, (255, 255, 255), (50 * i, 0), (50 * i, 450), 5)
            i += 1
        else:
            pygame.draw.line(win, (255, 255, 255), (50 * i, 0), (50 * i, 450), 1)
            i += 1
    i = 0
    for l in range(0, 10):
        if l % 3 == 0:
            pygame.draw.line(win, (255, 255, 255), (0, 50 * i), (450, 50 * i), 5)
            i += 1
        else:
            pygame.draw.line(win, (255, 255, 255), (0, 50 * i), (450, 50 * i), 1)
            i += 1


def drawbox(pos):
    if pos[0] <= 450 and pos[1] < 450:
        x = pos[0] // 50
        y = pos[1] // 50
        box = pygame.draw.rect(win, (0, 0, 255), (x * 50 + 1, y * 50 + 1, 49, 49), 4)


def wrong(wrongnumber1):
    i = 0
    wrongImg = pygame.image.load("heart.png")
    for x in range(wrongnumber1):
        win.blit(wrongImg, (i * 33, 460))
        i += 1


def printtime(start):
    sec=start%60
    min=sec//60
    timetxt= str(min)+":"+str(sec)
    timeImg= font.render("Time "+timetxt,True,(255,255,255))
    win.blit(timeImg,(300,455))


while run:
    win.fill((0, 0, 0))
    gridmaker()
    printboard(duplicate)
    timeplayed = round(time.time()-timestart)
    printtime(timeplayed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < 450 and pos[1] < 450:
                select = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and select:
                txt = 1
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_2 and select:
                txt = 2
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_3 and select:
                txt = 3
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_4 and select:
                txt = 4
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_5 and select:
                txt = 5
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_6 and select:
                txt = 6
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_7 and select:
                txt = 7
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_8 and select:
                txt = 8
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_9 and select:
                txt = 9
                updateboard(sudoku, duplicate, pos, txt)
            if event.key == pygame.K_DELETE and select:
                txt = 0
                updateboard(sudoku, duplicate, pos, txt)
                select = False
            if event.key == pygame.K_RETURN and select:
                issafe = checknum(duplicate, pos, txt)
                if issafe:
                    select = False
                else:
                    txt = 0
                    updateboard(sudoku, duplicate, pos, txt)
                    wrongnumber -= 1
            if event.key == pygame.K_SPACE:
                solveSudoku(sudoku)
                duplicate = sudoku
                printboard(sudoku)

    if select:
        drawbox(pos)

    if wrongnumber > 0:
        wrong(wrongnumber)
    else:
        over=pygame.image.load("over.png")
        win.blit(over,(98,150))
        go=font.render("Game Over",True,(255,0,0))
        win.blit(go,(130,115))
        pygame.display.update()
        pygame.time.delay(700)
        run=False

    pygame.display.update()

pygame.quit()

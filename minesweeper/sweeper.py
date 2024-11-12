import pygame
from board import Board

# Color scheme
BACKGROUND = (159, 148, 188)
BLACK = (0,0,0)
L_GREY = (200, 201, 202)
GREY = (140, 141, 141)

# Initial values of game
G_HEIGHT = 10
G_WIDTH = 25

C_HEIGHT = 40
C_WIDTH = 40

X_OFFSET = 200
Y_OFFSET = 20

grid = Board(G_HEIGHT, G_WIDTH, 50)

# Load necessary pictures for game
mine = pygame.image.load("media/mine.jpg")
mine = pygame.transform.scale(mine, (C_WIDTH, C_HEIGHT))

unseen = pygame.image.load("media/unseen.jpg")
unseen = pygame.transform.scale(unseen, (C_WIDTH, C_HEIGHT))

seen = pygame.image.load("media/seen.jpg")
seen = pygame.transform.scale(seen, (C_WIDTH, C_HEIGHT))

flag = pygame.image.load("media/flag.png")
flag = pygame.transform.scale(flag, (C_WIDTH, C_HEIGHT))

one = pygame.image.load("media/one.jpg")
one = pygame.transform.scale(one, (C_WIDTH, C_HEIGHT))

two = pygame.image.load("media/two.jpg")
two = pygame.transform.scale(two, (C_WIDTH, C_HEIGHT))

three = pygame.image.load("media/three.jpg")
three = pygame.transform.scale(three, (C_WIDTH, C_HEIGHT))

four = pygame.image.load("media/four.jpg")
four = pygame.transform.scale(four, (C_WIDTH, C_HEIGHT))

five = pygame.image.load("media/five.jpg")
five = pygame.transform.scale(five, (C_WIDTH, C_HEIGHT))

six = pygame.image.load("media/six.jpg")
six = pygame.transform.scale(six, (C_WIDTH, C_HEIGHT))

seven = pygame.image.load("media/seven.jpg")
seven = pygame.transform.scale(seven, (C_WIDTH, C_HEIGHT))

eight = pygame.image.load("media/eight.jpg")
eight = pygame.transform.scale(eight, (C_WIDTH, C_HEIGHT))

pygame.init()

back = pygame.display.set_mode((1600, 900))
board = pygame.surface.Surface((C_WIDTH * G_WIDTH, C_HEIGHT * G_HEIGHT))

back.fill(BACKGROUND)
board.fill(BLACK)
back.blit(board, (X_OFFSET, Y_OFFSET))

pygame.display.set_caption("Minesweeper")

# Load favicon
ico = pygame.image.load("media/flag.png")
pygame.display.set_icon(ico)


# creating a bool value which checks
# if game is running
running = True
clock = pygame.time.Clock()

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False


        # Handle mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            column = (pos[0] - X_OFFSET) // C_WIDTH
            row = (pos[1] - Y_OFFSET) // C_HEIGHT

            # If middle click or right click change flag value
            if event.button == 2 or event.button == 3:
                try:
                    grid.board[row][column].flag = True

                except IndexError:
                    pass

            elif event.button == 1:
                try:
                    grid.board[row][column].seen = True
                    if grid.board[row][column].value == 0:
                        grid.reveal(column, row)

                except IndexError:
                    pass

            print("Click ", pos, "Grid coordinates: ", row, column)

    for row in range(G_HEIGHT):
        for column in range(G_WIDTH):
            color = GREY
            cell = grid.board[row][column]
            if cell.seen:
                if cell.value == 1:
                    board.blit(one, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 2:
                    board.blit(two, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 3:
                    board.blit(three, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 4:
                    board.blit(four, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 5:
                    board.blit(five, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 6:
                    board.blit(six, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 7:
                    board.blit(seven, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == 8:
                    board.blit(eight, (C_WIDTH * column, C_HEIGHT * row))
                elif cell.value == -1:
                    board.blit(mine, (C_WIDTH * column, C_HEIGHT * row))
                else:
                    board.blit(seen, (C_WIDTH * column, C_HEIGHT * row))
            else:
                if cell.flag:
                    board.blit(flag, (C_WIDTH * column, C_HEIGHT * row))
                else:
                    board.blit(unseen, (C_WIDTH * column, C_HEIGHT * row))

            """
            pygame.draw.rect(board,
                             color,
                             [(MARGIN + C_WIDTH) * column + MARGIN,
                              (MARGIN + C_HEIGHT) * row + MARGIN,
                              C_WIDTH,
                              C_HEIGHT])
            """
    back.blit(board, (X_OFFSET, Y_OFFSET))
    clock.tick(50)
    pygame.display.flip()

pygame.quit()
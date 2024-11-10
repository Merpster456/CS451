import pygame

BACKGROUND = (159, 148, 188)
BLACK = (0,0,0)
L_GREY = (200, 201, 202)
GREY = (140, 141, 141)
MARGIN = 5

G_HEIGHT = 10
G_WIDTH = 25

C_HEIGHT = 25
C_WIDTH = 25

X_OFFSET = 200
Y_OFFSET = 20

pygame.init()

back = pygame.display.set_mode((1600, 900))
print((MARGIN + C_WIDTH) * (G_HEIGHT - 1) + MARGIN)
board = pygame.surface.Surface(((MARGIN + C_WIDTH) * (G_WIDTH - 1) + MARGIN, (MARGIN + C_HEIGHT) * (G_HEIGHT - 1) + MARGIN))

back.fill(BACKGROUND)
board.fill(BLACK)
back.blit(board, (X_OFFSET, Y_OFFSET))

pygame.display.set_caption("Minesweeper")

# Load favicon
ico = pygame.image.load("media/flag.png")
pygame.display.set_icon(ico)


grid = []
for row in range(G_HEIGHT):
    grid.append([])
    for col in range(G_WIDTH):
        grid[row].append(0)


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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            column = (pos[0] - X_OFFSET) // (C_WIDTH + MARGIN)
            row = (pos[1] - Y_OFFSET) // (C_HEIGHT + MARGIN)
            try:
                grid[row][column] = 1
            except IndexError:
                pass

            print("Click ", pos, "Grid coordinates: ", row, column)

    for row in range(G_HEIGHT):
        for column in range(G_WIDTH):
            color = GREY
            if grid[row][column] == 1:
                color = L_GREY
            pygame.draw.rect(board,
                             color,
                             [(MARGIN + C_WIDTH) * column + MARGIN,
                              (MARGIN + C_HEIGHT) * row + MARGIN,
                              C_WIDTH,
                              C_HEIGHT])
    back.blit(board, (X_OFFSET, Y_OFFSET))
    clock.tick(50)
    pygame.display.flip()

pygame.quit()
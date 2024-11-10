import pygame

BACKGROUND = (158, 149, 188)

class Cell:
    def __init__(self, value):
        self.value = value
        self.seen = False


c1 = Cell(1)

print(c1.seen)

pygame.init()

back = pygame.display.set_mode((1600, 900))
back.fill(BACKGROUND)
pygame.display.flip()
pygame.display.set_caption("Minesweeper")

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
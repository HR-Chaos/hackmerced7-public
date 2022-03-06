import pygame
from network import Network
# check episode 1 6:00 if network issue arises


# start by creating window
win_width = 600
win_height = 600
win = pygame.display.set_mode((win_width, win_height))  # double perenthesis needed becuz first argument is size
pygame.display.set_caption("client")

client_number = 0


# This player is a rectangle, it's used for testing the client
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        key_input = pygame.key.get_pressed()

        if key_input[pygame.K_LEFT]:
            self.x -= self.vel
        if key_input[pygame.K_RIGHT]:
            self.x += self.vel
        if key_input[pygame.K_UP]:
            self.y -= self.vel
        if key_input[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):  # tup = tuple
    return str(tup[0]) + "," + str(tup[1])


# redraws the window, call with whatever you want to be redrwan
def redraw_window(win, player, player2):
    win.fill((255, 255, 255))       # double perenthesis needed again becuz it is one argument
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


# main function that runs continuously
def main():
    run = True
    clock = pygame.time.Clock()
    col = (0, 255, 0)

    # This makes the network var so that we don't have to do it multiple times
    n = Network()
    start_pos = read_pos(n.get_pos())
    p = Player(start_pos[0], start_pos[1], 30, 30, col)
    p2 = Player(0, 0, 30, 30, col)

    # while game is running
    while run:
        clock.tick(60)

        p2pos = read_pos(n.send(make_pos((p.x, p.y))))  # send position of you to get pos of p2 so you can draw p2
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(win, p, p2)


main()

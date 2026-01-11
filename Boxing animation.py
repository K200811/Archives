# Made on 3/8/2024 at 7:14PM
# Creates two static boxers using Pygame. The purpose of this project was to teach me how to use Pygame.
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
OpenGL_accelerate

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boxing Animation")

# Boxer positions
boxer1_x, boxer1_y = WIDTH // 4, HEIGHT // 2
boxer2_x, boxer2_y = 3 * WIDTH // 4, HEIGHT // 2

def draw_boxer(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 50, y)
    glVertex2f(x + 50, y + 50)
    glVertex2f(x, y + 50)
    glEnd()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        draw_boxer(boxer1_x, boxer1_y)
        draw_boxer(boxer2_x, boxer2_y)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
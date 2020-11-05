from PIL import Image
from tkinter import *
import pygame


def main():
    pygame.init()
    pygame.joystick.init()

    print(pygame.joystick.get_count())

    joystick = pygame.joystick.Joystick(0)

    buttons = {
        'left': joystick.get_button(7),
        'right': joystick.get_button(5),
        'up': joystick.get_button(4),
        'down': joystick.get_button(6),
        'square': joystick.get_button(15),
        'x': joystick.get_button(14),
        'circle': joystick.get_button(13),
        'triangle': joystick.get_button(12),
        'r1': joystick.get_button(11),
        'r2': joystick.get_button(9),
        'l1': joystick.get_button(10),
        'l2': joystick.get_button(8),
        'select': joystick.get_button(0),
        'start': joystick.get_button(3),
        'l3': joystick.get_button(1),
        'r3': joystick.get_button(2),
        'ps': joystick.get_button(16),
    }

    display_width = 60
    display_height = 180

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Lunky Helper')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    orb_image = pygame.image.load('hiclipart.com.png')

    x = 0
    y = 0

    count = 1
    while not crashed:
        game_display.fill(black)

        if count > 0:
            game_display.blit(orb_image, (x, y))
        if count > 1:
            game_display.blit(orb_image, (x, y + 60))
        if count > 2:
            game_display.blit(orb_image, (x, y + 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    count = cycle_count(count)
            elif event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(10):
                    count = cycle_count(count)

        pygame.display.update()
        clock.tick(60)

    pygame.joystick.quit()
    pygame.quit()
    quit()


def cycle_count(count):
    if count > 2:
        count = -1
    count = count + 1
    return count


if __name__ == "__main__":
    main()

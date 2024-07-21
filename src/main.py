# This is a sample Python arkanoid game.

import pygame
import pygame.display as display

from pygame import Surface, Vector2
from pygame.time import Clock

from engine.game_initializer import initialize_game
from graphics import render
from objects.game_object import GameObject


def main() -> None:
    # pygame setup
    pygame.init()

    screen_size: Vector2 = Vector2(800, 500)
    screen: Surface = display.set_mode(screen_size)
    screen_center: Vector2 = Vector2(screen.get_width() / 2, screen.get_height() / 2)

    clock: Clock = pygame.time.Clock()
    delta: float = 0.00

    game_objects: list[GameObject] = initialize_game(screen_center, screen_size)

    running: bool = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        render.render(screen, game_objects)

        # flip() the display to put your work on screen
        display.flip()

        delta = clock.tick(60)  # limits FPS to 60 & returns current frame time

    pygame.quit()


if __name__ == "__main__":
    main()

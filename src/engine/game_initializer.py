from pygame import Vector2

from objects.ball import Ball
from objects.game_object import GameObject


def initialize_game(screen_center: Vector2, screen_size: Vector2) -> list[GameObject]:
    game_objects: list[GameObject] = []

    game_objects.append(Ball(screen_center, 0.0, 1.0, Vector2(0.0, 0.0), 5.0, False))

    return game_objects

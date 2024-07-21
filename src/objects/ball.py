import pygame
from pygame import Surface, Vector2

from objects.game_object import GameObject


class Ball(GameObject):
    __radius: float

    def __init__(
        self,
        pos: Vector2,
        speed: float,
        scale: float,
        direction: Vector2,
        radius: float,
        is_moving: bool,
    ):
        super().__init__(pos, speed, scale, direction, is_moving)
        self.__radius = radius

    def check_collision(self, collision_pos: Vector2) -> bool: ...

    def draw(self, surface: Surface) -> None:
        pygame.draw.circle(surface, "white", self.get_pos(), self.__radius)

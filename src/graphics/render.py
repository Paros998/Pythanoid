from pygame import Surface

from objects.game_object import GameObject


def render(screen: Surface, objects: list[GameObject]) -> None:
    for obj in objects:
        obj.draw(screen)

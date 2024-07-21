from abc import ABC, abstractmethod
from pygame import Vector2, Surface


class GameObject:
    __initial_pos: Vector2
    __pos: Vector2
    __speed: float
    __scale: float
    __direction: Vector2
    __is_moving: bool

    def __init__(self, pos: Vector2, speed: float, scale: float, direction: Vector2, is_moving: bool):  # type: ignore
        self.__initial_pos = pos
        self.__pos = pos
        self.__speed = speed
        self.__scale = scale
        self.__direction = direction
        self.__is_moving = is_moving

    def move(self, new_pos: Vector2) -> None:
        self.__pos = new_pos

    def reset_position(self) -> None:
        self.__pos = self.__initial_pos

    def get_pos(self) -> Vector2:
        return self.__pos

    def get_speed(self) -> float:
        return self.__speed

    def change_direction(self, new_direction: Vector2) -> None:
        self.__direction = new_direction

    def get_direction(self) -> Vector2:
        return self.__direction

    def should_calculate_movement(self) -> bool:
        return self.__is_moving

    @abstractmethod
    def draw(self, surface: Surface) -> None:
        pass

    @abstractmethod
    def check_collision(self, collision_pos: Vector2) -> bool:
        pass

from pygame import Vector2

from objects.game_object import GameObject
from utilities.utils import Direction


def move_object(game_object: GameObject) -> None:
    calculated_position: Vector2 = game_object.get_pos() + (
        game_object.get_direction() * game_object.get_speed()
    )
    game_object.move(calculated_position)


def face_direction(game_object: GameObject, direction: Direction) -> None:
    current_direction = game_object.get_direction()
    match direction:
        case Direction.UP:
            if current_direction.y < 0:
                face_other_y_axis_direction(game_object)
        case Direction.DOWN:
            if current_direction.y > 0:
                face_other_y_axis_direction(game_object)
        case Direction.LEFT:
            if current_direction.x < 0:
                face_other_x_axis_direction(game_object)
        case Direction.RIGHT:
            if current_direction.x > 0:
                face_other_x_axis_direction(game_object)


def face_other_x_axis_direction(game_object: GameObject) -> None:
    direction = game_object.get_direction()
    direction.x *= -1.0
    # TODO check if necessary
    # game_object.change_direction(direction)


def face_other_y_axis_direction(game_object: GameObject) -> None:
    direction = game_object.get_direction()
    direction.y *= -1.0
    # TODO check if necessary
    # game_object.change_direction(direction)

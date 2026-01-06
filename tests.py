import pytest
from main import SpaceShip, Vector, Move


class TestMovable:

    def test_move_correct(self):
        space_ship = SpaceShip(coords=Vector(1,1), velocity=Vector(7, -5), angle=5)
        move = Move(space_ship)
        move.execute()
        assert space_ship.get_position() == Vector(8, -4)

    def test_move_incorrect_coords(self):
        space_ship = SpaceShip(coords=None, velocity=Vector(7, -5), angle=5)
        move = Move(space_ship)
        with pytest.raises(ValueError) as err:
            move.execute()
            space_ship.get_position()

    def test_move_incorrect_velocity(self):
        space_ship = SpaceShip(coords=Vector(1,1), velocity=None, angle=5)
        move = Move(space_ship)
        with pytest.raises(ValueError) as err:
            move.execute()
            space_ship.get_position()



class Vector:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y


class MovableAbstract:

    def __init__(self, *, coords: tuple | Vector = None, velocity: tuple | Vector = None, **kwargs):
        super().__init__(**kwargs)
        if isinstance(coords, tuple):
            self.position = Vector(*coords)
        else:
            self.position = coords
        if isinstance(velocity, tuple):
            self.velocity = Vector(*velocity)
        else:
            self.velocity = velocity

    def get_velocity(self):
        return self.velocity
    
    def get_position(self):
        return self.position
    
    def set_position(self, value: Vector):
        if not isinstance(value, Vector):
            raise ValueError('Incorrect type argument for set_position method.')
        self.position = value


class RotateAbstract:

    def __init__(self, *, angle: float, **kwargs):
        super().__init__()
        if not isinstance(angle, (float, int)):
            raise ValueError('Incorrect value for angle')
        self.angle = angle

    def get_angle(self):
        return self.angle

    def set_angle(self, value: int):
        self.angle = value


class Move:

    def __init__(self, movable_object: MovableAbstract):
        self.movable = movable_object

    def execute(self):
        if not self.movable.get_position():
            raise ValueError('Can`t get object`s position')
        if not self.movable.get_velocity():
            raise ValueError('Can`t get object`s velocity')
        self.movable.set_position(self.movable.get_position() + self.movable.get_velocity())


class SpaceShip(MovableAbstract, RotateAbstract):
    ...


class Torpeda(MovableAbstract):
    ...

import math
import raylibpy as rl

# Constants
WIDTH = 800
HEIGHT = 600
FRICTION_FORCE = 1000.0 # Newtons

class Vector2:
    def __init__(self, x: float = 0.0, y: float= 0.0):
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, vec: 'Vector2'):
        assert(isinstance(vec, Vector2))

        return Vector2(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec: 'Vector2'):
        assert(isinstance(vec, Vector2))

        return Vector2(self.x - vec.x, self.y - vec.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar: float):
        assert(isinstance(scalar, (int, float)))

        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar: float):
        assert(isinstance(scalar, (int, float)))

        return Vector2(self.x / scalar, self.y / scalar)

    def __rtruediv__(self, scalar):
        return self.__truediv__(scalar)
    
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def normalized(self):
        return self / self.length()

class Car:
    def __init__(self):
        self.position: Vector2 = Vector2(100, 100)
        self.velocity: Vector2 = Vector2(1000.0, 100.0)
        self.mass = 500 # kg

    # def calculate_drag(self) -> Vector2:
    #     if 
    def get_friction_force(self):
        if self.velocity.length() > 0.0:
            return FRICTION_FORCE * -self.velocity.normalized()
        else:
            return Vector2()

    # Process physics?
    def process(self):
        total_force: Vector2 = self.get_friction_force()

        self.velocity += total_force * rl.get_frame_time()

        self.position += self.velocity * rl.get_frame_time()

    def draw(self):
        rl.draw_texture(car_texture, self.position.x, self.position.y, rl.WHITE)


if __name__ == "__main__":
    rl.init_window(WIDTH, HEIGHT, "Formula-1 Racing")

    car_image = rl.load_image("assets/car_hull.png")
    rl.image_resize(car_image, 62, 142)
    car_texture = rl.load_texture_from_image(car_image)

    car = Car()

    while not rl.window_should_close():
        rl.begin_drawing()

        rl.clear_background(rl.WHITE)

        car.process()
        car.draw()

        rl.end_drawing()
    
    rl.close_window()
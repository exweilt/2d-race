import pygame

# Constants
WIDTH = 800
HEIGHT = 600

class Car:
    def __init__(self):
        self.position = (100, 100)

    def draw(self):
        screen.blit(car_texture, (100, 100))

if __name__ == "__main__":

    # Initialization
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    texture = pygame.image.load("assets/car_hull.png")
    car_texture = pygame.transform.scale(texture, (62, 142))

    car = Car()

    # Main Window Loop
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Display
        screen.fill((255, 255, 255))
        car.draw()
        

        pygame.display.flip()

    pygame.quit()
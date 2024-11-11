import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        for object in asteroids:
            if object.check_collision(player):
                print("Game over!")
                return
        clock.tick(60)
        dt = clock.tick(60)/1000
        pygame.display.flip()
        


if __name__ == "__main__":
    main()

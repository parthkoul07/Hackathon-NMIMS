import pygame, asyncio
import random

pygame.init()
async def main():
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Random Points Connector")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    points = []
    connections = []

    max_points = random.randint(5, 15)

    for _ in range(max_points):
        points.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    for i in range(len(points)):
        available_indices = [j for j in range(len(points)) if
                             j != i and (i, j) not in connections and (j, i) not in connections]
        chosen_connections = random.sample(available_indices, min(2, len(available_indices)))
        for j in chosen_connections:
            connections.append((i, j))

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for point in points:
            pygame.draw.circle(screen, RED, point, 5)

        for i, j in connections:
            pygame.draw.line(screen, WHITE, points[i], points[j], 1)

        pygame.display.flip()
        pygame.time.delay(100)


    await asyncio.sleep(0)

asyncio.run(main())
pygame.quit()
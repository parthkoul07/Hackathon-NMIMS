
import pygame
import asyncio
import os
# COMPLETELY DISABLE ALL REMOTE TEMPLATE FETCHING
os.environ["PYGBAG_TEMPLATE_URL"] = "0"  # "0" means no remote fetching
os.environ["PYGBAG_BACKEND"] = "webgl"
os.environ["PYGBAG_FULLSCREEN"] = "1"
os.environ["PYGBAG_CACHE"] = "0"  # Disable caching

async def main():
    # Initialize pygame PROPERLY for web
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Your game setup code here
    clock = pygame.time.Clock()
    running = True

    # MAIN GAME LOOP
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Your game rendering/updates here
        screen.fill((0, 0, 0))
        pygame.display.flip()
        await asyncio.sleep(0)  # CRUCIAL for browser rendering
        clock.tick(60)


# This ensures proper startup
if __name__ == "__main__":
    asyncio.run(main())
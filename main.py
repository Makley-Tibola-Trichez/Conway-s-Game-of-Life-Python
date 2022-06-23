import sys
import random
import numpy as np
import pygame

GRID_SIZE = 70
LIVE_CELL_COLOR = (255, 255, 255)

grid = np.zeros((GRID_SIZE, GRID_SIZE))


def main():
    screen = create_screen()
    _grid = insert_cells_in_grid()
    while True:
        screen.fill((0, 0, 0))
        draw_grid(_grid, screen)
        _grid = update_grid(_grid)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    _grid = insert_cells_in_grid()

            close_game(event)


def insert_cells_in_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            _random_value = random.randrange(0, 100)
            grid[i][j] = 1 if _random_value >= 70 else 0
    return grid


def create_screen():
    pygame.init()
    pygame.display.set_caption('Game of Life')
    return pygame.display.set_mode((GRID_SIZE * 10, GRID_SIZE * 10))


def close_game(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def draw_grid(grid, _screen):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
                pygame.draw.rect(_screen, LIVE_CELL_COLOR,
                                 (i * 10, j * 10, 10, 10))
    pygame.display.update()


def update_grid(grid):
    temp_grid = grid.copy()

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            neightbours_count = count_neighbours(temp_grid, x, y)

            if neightbours_count < 2 or neightbours_count > 3:
                grid[x, y] = 0

            elif neightbours_count == 3:
                grid[x, y] = 1

    return grid


def count_neighbours(grid, x, y):
    x_max = (x+1) % GRID_SIZE
    y_max = (y+1) % GRID_SIZE

    positions = [
        (x-1, y),
        (x_max, y),
        (x-1, y_max),
        (x, y_max),
        (x_max, y_max),
        (x, y-1),
        (x-1, y-1),
        (x_max, y-1),
    ]

    c_neightbors_live = 0
    for p in positions:
        c_neightbors_live += grid[p]

    return c_neightbors_live


if __name__ == '__main__':
    main()

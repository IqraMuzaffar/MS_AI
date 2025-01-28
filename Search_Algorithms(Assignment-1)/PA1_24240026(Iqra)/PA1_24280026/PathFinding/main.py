import pygame
import random
import numpy as np
from bfs import Bfs
from dfs import Dfs
from A_star import A_star

pygame.init()

GRID_SIZE = 15
CELL_SIZE = 25
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
WINDOW_WIDTH = 3 * WINDOW_SIZE + 40 
WINDOW_HEIGHT = WINDOW_SIZE + 60  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TITLE_COLOR = (255, 255, 255)
BORDER_COLOR = (39, 75, 222)
STEP_DELAY = 100  
FONT = pygame.font.SysFont(None, 24)
TITLE_FONT = pygame.font.SysFont(None, 36)
YELLOW = (255, 255, 0)
PACMAN_COLOR = YELLOW
ENEMY_COLOR = RED

def create_grid(size, START, END, obstacle_prob=0.15):
    grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_prob and (i, j) not in [START, END]:
                grid[i][j] = 1 
            if grid[i][j] != 1:
                grid[i][j] = random.randint(1, 20)  
    return grid

def validate_list(variable , algo):
    RED = "\033[91m"
    RESET = "\033[0m"
    
    if not isinstance(variable, list):
        raise TypeError(f"{RED}Error: The Function {algo} did not return a  not a list.{RESET}")
    
    if not all(isinstance(item, tuple) for item in variable):
        raise ValueError(f"{RED}Error: The Function {algo} returned a list but the list contain one or many non tuples.{RESET}")


def calculate_path_cost(Grid, path):
    return sum(Grid[x][y] for x, y in path)

def draw_pacman(screen, x, y, size, direction='right'):
    center = (x + size // 2, y + size // 2)
    pygame.draw.circle(screen, PACMAN_COLOR, center, size // 2)
    
    # Draw Pac-Man's mouth based on direction
    mouth_rect = pygame.Rect(x + size // 4, y, size // 2, size // 2)
    if direction == 'right':
        pygame.draw.polygon(screen, BLACK, [(x + size // 2, y + size // 2), 
                                            (x + size, y), 
                                            (x + size, y + size)])
    elif direction == 'left':
        pygame.draw.polygon(screen, BLACK, [(x + size // 2, y + size // 2), 
                                            (x, y), 
                                            (x, y + size)])
    elif direction == 'up':
        pygame.draw.polygon(screen, BLACK, [(x + size // 2, y + size // 2), 
                                            (x, y), 
                                            (x + size, y)])
    elif direction == 'down':
        pygame.draw.polygon(screen, BLACK, [(x + size // 2, y + size // 2), 
                                            (x, y + size), 
                                            (x + size, y + size)])

def draw_enemy(screen, x, y, size):
    center = (x + size // 2, y + size // 2)
    pygame.draw.circle(screen, ENEMY_COLOR, center, size // 2)

    # Draw enemy eyes
    eye_radius = size // 8
    eye_x_offset = size // 4
    eye_y_offset = size // 4
    pygame.draw.circle(screen, BLACK, (center[0] - eye_x_offset, center[1] - eye_y_offset), eye_radius)
    pygame.draw.circle(screen, BLACK, (center[0] + eye_x_offset, center[1] - eye_y_offset), eye_radius)

    # Draw angry expression (eyebrows)
    pygame.draw.line(screen, BLACK, (center[0] - eye_x_offset - eye_radius, center[1] - eye_y_offset - eye_radius), 
                     (center[0] - eye_radius, center[1] - eye_y_offset), 2)
    pygame.draw.line(screen, BLACK, (center[0] + eye_x_offset + eye_radius, center[1] - eye_y_offset - eye_radius), 
                     (center[0] + eye_radius, center[1] - eye_y_offset), 2)

def draw_grid(screen, Grid, path, explored, START, END, offset, title, current_node=None):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if (i, j) == START:
                pygame.draw.rect(screen, GREEN, rect)
            elif (i, j) == END:
                pygame.draw.rect(screen, BLACK, rect)
                draw_enemy(screen, j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE)
            elif (i, j) in path:
                pygame.draw.rect(screen, RED, rect)
            elif (i, j) in explored:
                pygame.draw.rect(screen, GRAY, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
            
            pygame.draw.rect(screen, WHITE, rect, 1)  # 1 pixel wide border
            
            if Grid[i][j] != 1 and (i,j) != END:
                text = FONT.render(str(int(Grid[i][j])), True, WHITE)
                screen.blit(text, (j * CELL_SIZE + offset + 5, i * CELL_SIZE + 5))
                
            if (i, j) == current_node:
                draw_pacman(screen, j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, direction='right')  # Example direction

    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(offset, 0, WINDOW_SIZE, WINDOW_SIZE), 3)
    title_text = TITLE_FONT.render(title, True, TITLE_COLOR)
    screen.blit(title_text, (offset + 10, WINDOW_SIZE + 10))

def step_by_step_visualization(screen, Grid, path, explored, START, END, offset, title, clear_previous=False):
    if clear_previous:
        draw_grid(screen, Grid, path, explored, START, END, offset, title)
    for step in range(len(explored)):
        current_node = explored[step]
        draw_grid(screen, Grid, path, explored[:step + 1], START, END, offset, title, current_node)
        pygame.display.flip()
        pygame.time.wait(STEP_DELAY)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("PacMan PathFinding")

    clock = pygame.time.Clock()

    START = (random.randint(0, 3), random.randint(0, GRID_SIZE - 1))
    END = (random.randint(GRID_SIZE - 4, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    Grid = create_grid(GRID_SIZE, START, END)

    bfs_path, bfs_explored = Bfs(Grid, START, END, GRID_SIZE)
    dfs_path, dfs_explored = Dfs(Grid, START, END, GRID_SIZE)
    a_star_path, a_star_explored = A_star(Grid, START, END, GRID_SIZE)

    try:
        validate_list(bfs_path , 'Bfs')
        validate_list(bfs_explored , 'Bfs')
        validate_list(dfs_path , 'Dfs')
        validate_list(dfs_explored , 'Dfs')
        validate_list(a_star_path , 'A-star')
        validate_list(a_star_explored , 'A-star')

    except (TypeError, ValueError) as e:
        print(e)
        return 0


    bfs_cost = calculate_path_cost(Grid, bfs_path)
    dfs_cost = calculate_path_cost(Grid, dfs_path)
    a_star_cost = calculate_path_cost(Grid, a_star_path)

    draw_grid(screen, Grid, [], [], START, END, 0, f"BFS Path (Cost: {bfs_cost})")
    draw_grid(screen, Grid, [], [], START, END, WINDOW_SIZE + 10, f"DFS Path (Cost: {dfs_cost})")
    draw_grid(screen, Grid, [], [], START, END, 2 * WINDOW_SIZE + 20, f"A* Path (Cost: {a_star_cost})")
    pygame.display.flip()

    # Visualize BFS exploration step by step
    step_by_step_visualization(screen, Grid, [], bfs_explored, START, END, 0, f"BFS Path (Cost: {bfs_cost})")
    draw_grid(screen, Grid, bfs_path, bfs_explored, START, END, 0, f"BFS Path (Cost: {bfs_cost})")
    pygame.display.flip()
    pygame.time.wait(2000)  

    # Visualize DFS exploration step by step
    step_by_step_visualization(screen, Grid, [], dfs_explored, START, END, WINDOW_SIZE + 10, f"DFS Path (Cost: {dfs_cost})")
    draw_grid(screen, Grid, dfs_path, dfs_explored, START, END, WINDOW_SIZE + 10, f"DFS Path (Cost: {dfs_cost})")
    pygame.display.flip()
    pygame.time.wait(2000) 

    # Visualize A* exploration step by step
    step_by_step_visualization(screen, Grid, [], a_star_explored, START, END, 2 * WINDOW_SIZE + 20, f"A* Path (Cost: {a_star_cost})")
    draw_grid(screen, Grid, a_star_path, a_star_explored, START, END, 2 * WINDOW_SIZE + 20, f"A* Path (Cost: {a_star_cost})")
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()

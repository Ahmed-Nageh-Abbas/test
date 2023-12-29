#bfs_algo
import copy
from board import boards
from collections import deque
import pygame
import math
import heapq

pygame.init()


WIDTH = 720
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH, HEIGHT])
num1 = ((HEIGHT-50) // 32)
num2 = (WIDTH // 30)
timer = pygame.time.Clock()
fps =15
level = copy.deepcopy(boards)
color = 'red'
PI = math.pi
player_image_r = pygame.transform.scale(pygame.image.load('assets/player_images/4_r.png'), (45, 45))
player_image_l = pygame.transform.scale(pygame.image.load('assets/player_images/4_l.png'), (45, 45))
player_image_u = pygame.transform.scale(pygame.image.load('assets/player_images/4_u.png'), (45, 45))
player_image_d = pygame.transform.scale(pygame.image.load('assets/player_images/4_d.png'), (45, 45))
player_x = num2*2
player_y = num1*2
direction = 0

def draw_board():
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def draw_player():
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
    n1 =  (0.5 * num1)
    n2 =  (0.5 * num2)
    p_rect = player_image_r.get_rect(center=(player_x+n1, player_y+n2))
    if direction == 0:
        screen.blit(player_image_r, p_rect)
    elif direction == 1:
        screen.blit(player_image_l, p_rect)
    elif direction == 2:
        screen.blit(player_image_u, p_rect)
    elif direction == 3:
        screen.blit(player_image_d, p_rect)
   


def is_valid(x, y, level):
    return 0 <= x < 33 and 0 <= y < 30 and 0 <= level[x][y] <= 2 # ---->Check if within road and not a wall 

def heuristic_function(x,y): return 30-x+27-y
def a_star(level, start, end):
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
    queue = [(heuristic_function(2,2), start, [], 0)]
    while queue:
        l = heapq.heappop(queue)
        print(l)
        (x, y) = l[1]
        path = l[2]
        if (x, y) == end:
            return path
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, level):
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    heapq.heappush(queue, (l[3] + 1 + heuristic_function(x,y), (new_x, new_y), path + [(new_x, new_y)], l[3]+1))

path_to_target = a_star(level, (2, 2), (30 , 27))
index=0

run = True
while run:
    timer.tick(fps)

    screen.fill('black')
    
    if index < len(path_to_target):
        next_position = path_to_target[index]
        next_y = next_position[0] * num1
        next_x = next_position[1] * num2
        if next_x > player_x: direction = 0
        if next_x < player_x: direction = 1
        if next_y < player_y: direction = 2
        if next_y > player_y: direction = 3
        player_x = next_x
        player_y = next_y
        index += 1

    draw_board()
    draw_player()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(len(level)):
        for j in range(len(level[0])):
            pygame.draw.circle(screen, 'blue', (num2*j + (0.5*num2) , num1*i + (0.5*num1)), 5)

    pygame.display.flip()
pygame.quit()

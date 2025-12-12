import pygame
import time
from food import Food
from snake import Snake

while True:
    num_foods = int(input("How many pieces of food do you want?"))
    if num_foods >0:
        break
    print("Number must be 1 or above!")

while True:
    num_b_foods = int(input("How many pieces of booby food do you want?"))
    if num_b_foods >0:
        break
    print("Number must be 1 or above!")
# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("ThaT_sNake_GamE")

score = 0
font = pygame.font.SysFont("biome", 20)
COLOR_bg = (0, 128, 146)
COLOR_snake1 = (255, 0, 57)
COLOR_snake2 = (0, 255, 0)
COLOR_food = (78, 0, 0)
COLOR_food2 = (71, 3, 43)


            
foods = [Food()for i in range(num_foods)]
boooooooooby_food = Food()
snake1 = Snake()
snake2 = Snake()

clock = pygame.time.Clock()


def collided1(food):
    if snake1.head == food.location:
        global score
        score += 1
        return True   
    
    else:
        return False

def collided2(food):
    if snake2.head == food.location:
        global score
        score += 1
        return True   
    
    else:
        return False

running = True

while running:
    screen.fill(COLOR_bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake1.change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake1.change_direction = 'RIGHT'
            if event.key == pygame.K_UP:
                snake1.change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                snake1.change_direction = 'DOWN'    


            if event.key == pygame.K_w:
                snake2.change_direction = 'UP'
            if event.key == pygame.K_s:
                snake2.change_direction = 'DOWN'
            if event.key == pygame.K_a:
                snake2.change_direction = 'LEFT'
            if event.key == pygame.K_d:
                snake2.change_direction = 'RIGHT'

    if snake1.alive:
        for block in snake1.body:
            pygame.draw.rect(screen, COLOR_snake1, pygame.Rect(block[0], block[1], 10, 10))
        snake1.move()
    if snake2.alive:
        for block in snake2.body:
            pygame.draw.rect(screen, COLOR_snake2, pygame.Rect(block[0], block[1], 10, 10))
        snake2.move()

    pygame.draw.rect(screen, COLOR_food2, pygame.Rect(boooooooooby_food.location[0], boooooooooby_food.location[1], 10, 10))
    if snake1.head == boooooooooby_food.location:
        print("You ate the poisonous candy and died!!!!!")
        snake1.alive = False

    if snake2.head == boooooooooby_food.location:
        print("You ate the poisonous candy and died!!!!!")
        snake2.alive = False

    if snake1.alive == False and snake2.alive == False:
        running = False


    for food in foods:
        pygame.draw.rect(screen, COLOR_food, pygame.Rect(food.location[0], food.location[1], 10, 10))

        if collided1(food):
            snake1.add_length(True)
            food.respawn_parameter()

        else:
            snake1.add_length(False)

        if collided2(food):
            snake2.add_length(True)
            food.respawn_parameter()

        else:
            snake2.add_length(False)


    if snake1.hit_body():
        snake1.alive = False    
    if snake1.hit_wall(600, 400):
        snake1.alive = False

    if snake2.hit_body():
        snake2.alive = False    
    if snake1.hit_wall(600, 400):
        snake2.alive = False


    score_text = font.render(f'Score: {score}',True,(0, 0, 0))
    screen.blit(score_text, (10, 10))


    pygame.display.update()
    clock.tick(10)
print("You Died!!!!!!!")
print(f"Your score is {score}!")

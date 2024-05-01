#! bin/python3




import enum
import math
import time
import pygame
import random
import warnings
from typing import List, Tuple


pygame.init()
pygame.font.init()
display_width, display_height = (1440, 810)
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)




def write(msg: str, color: Tuple[int], pos: Tuple[int], size: int, aa: bool = True, centered: bool = False) -> None:
    font = pygame.font.SysFont("fontawsome", size)
    surface = font.render(msg, aa, color)
    if centered:
        pos = surface.get_rect(center=(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2))
    display.blit(surface, (pos[0], pos[1]))


def translate_pos2idx(pos: Tuple[int]) -> Tuple[int]:
    return ((pos[1] - 100) // 32, (pos[0] - 100) // 32)


def translate_idx2pos(index: Tuple[int]) -> Tuple[int]:
    return (index[1] * 32 + 100 + 16, index[0] * 32 + 100 + 16)



class Direction(enum.Enum):
    "Position changes are index based"
    NORTH = (-1, 0, 3)
    EAST = (0, 1, 0)
    SOUTH = (1, 0, 1)
    WEST = (0, -1, 2)



class Snake(object):
    "POSITIONS are handled as index"
    head_image = pygame.image.load("resources/snake_head.png")
    body_image = pygame.image.load("resources/snake_body.png")
    def __init__(self, parts: List[Tuple[int]], direction: Direction = Direction.EAST) -> None:
        self.parts: List[Tuple[int]] = parts
        self.direction = direction
    
    def grow(self, size: int = 1) -> None:
        for _ in range(size):
            self.parts.append(((self.parts[-1][0] + self.direction.value[0])%19, (self.parts[-1][1] + self.direction.value[1])%32)) 

    def update(self, direction):
        # Do not change direction when new direction point into opposite direction
        if self.direction.value[0] + direction.value[0] == 0 and self.direction.value[1] + direction.value[1] == 0:
            direction = self.direction
        self.direction = direction
        self.parts.append(((self.parts[-1][0] + direction.value[0])%19, (self.parts[-1][1] + direction.value[1])%32)) 
        del self.parts[0]

    def draw(self) -> None:
        for index, part in enumerate(self.parts):
            pos = translate_idx2pos(part)
            if index == len(self.parts) - 1:
                display.blit(pygame.transform.rotate(Snake.head_image, self.direction.value[2] * 90), (pos[0] - 16, pos[1] - 16))
            elif index == 0:
                pygame.draw.circle(display, 0x12e012, translate_idx2pos(part), 16, 0)
            else:
                pygame.draw.circle(display, 0x12e012, translate_idx2pos(part), 16, 0)
                #display.blit(pygame.transform.rotate(Snake.body_image, self.direction.value[2] * 90), (pos[0] - 16, pos[1] - 16))


class Consumable(object):
    "POSITIONS are handles as index"
    def __init__(self, pos: Tuple[int], lifetime: int = 30) -> None:
        self.pos = pos
        self.birth = time.time()
        self.lifetime = lifetime
        self.death = self.birth + self.lifetime
        self.is_alive = True

    def update(self) -> None:
        if time.time() >= self.death:
            self.is_alive = False
    
    def _consume(self) -> int:
        warnings.warn("Consumeable.consume() has not been implemented, consumable will not have any effects")
        return 0

    def consume(self) -> int:
        if self.is_alive:
            return self.value
        return 0
    
    def _draw(self) -> None:
        warnings.warn("Consumeable.draw() has not been implemented, consumable will not be drawn")

    def draw(self) -> None:
        if self.is_alive:
            self._draw()



class Fruit(Consumable):
    def __init__(self, pos: Tuple[int], image) -> None:
        super().__init__(pos)
        self.image = image
        self.value = 1

    def _draw(self) -> None:
        pos = translate_idx2pos(self.pos)
        display.blit(self.image, (pos[0] - 16, pos[1] - 16))
        

class Apple(Fruit):
    image = pygame.image.load("resources/apple.png")
    def __init__(self, pos: Tuple[int]) -> None:
        super().__init__(pos, Apple.image)
        self.value = 2


class Cherry(Fruit):
    image = pygame.image.load("resources/cherry.png")
    def __init__(self, pos: Tuple[int]) -> None:
        super().__init__(pos, Cherry.image)



class App(object):
    def __init__(self):
        pass

    def main(self) -> None:
        running = True
        animation_speed = 64 
        while running:
            mouse_pos = pygame.mouse.get_pos() 
            display.fill((0xe0, 0xbb, 0xe4))
            
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        pygame.quit()
                        quit()
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                running = False
                            
                            case pygame.K_SPACE:
                                self.game()

            write("Press SPACE to start", (0xaa, 0x1b, 0x8c), (0, 0, display_width, display_height), int(120 + math.sin(pygame.time.get_ticks() / animation_speed)*16), centered=True)
            write("Snake alpha1.0", (0xaa, 0x1b, 0x8c), (16, 16), 32)
            
            color = (0xcc, 0x14, 0x51)
            if pygame.mouse.get_pressed()[0]:
                color = (0x14, 0xcc, 0x51)
            pygame.draw.circle(display, color, mouse_pos, 16, 0)
            
            
            clock.tick(144)
            pygame.display.update()

    
    def game(self) -> None:
        running = True
        snake = Snake([(10, 2), (10, 3)])
        fruit = Apple((random.randint(0, 16), random.randint(0, 32)))
        direction: Direction = Direction.EAST
        snake_update_time = time.time()
        input_buffer = []
        while running:
            display.fill((0xe0, 0xbb, 0xe4))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        pygame.quit()
                        quit()
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                running = False
                            
                            # Capture movement inputs
                            case pygame.K_UP:
                                direction = Direction.NORTH
                            case pygame.K_RIGHT:
                                direction = Direction.EAST
                            case pygame.K_DOWN:
                                direction = Direction.SOUTH
                            case pygame.K_LEFT:
                                direction = Direction.WEST
           
            # Make sure to capture all inputs in between snake updates using a buffer
            if len(input_buffer) > 0:
                if input_buffer[-1] != direction:
                    input_buffer.append(direction)
            else:
                input_buffer.append(direction)


            # Drawing grid
            for row in range(19):
                for column in range(32):
                    pygame.draw.rect(display, 0x000000, (100 + column*32, 100 + row*32, 32, 32), 1)


            # Chek if fruit is still alive and replace otherwise 
            if not fruit.is_alive:
                if random.randint(0, 1) == 0:
                    fruit = Apple((random.randint(0, 18), random.randint(0, 31)))
                else:
                    fruit = Cherry((random.randint(0, 18), random.randint(0, 31)))


            # Update snake movement based on direction inputs
            if time.time() - snake_update_time >= .1:
                snake.update(input_buffer[0])
                snake_update_time = time.time()
                del input_buffer[0]

                # Check if snake hit obstacle
                for part in snake.parts[:-1]:
                    if part == snake.parts[-1]:
                        running = False

            
            # Check if snake ate fruit
            if fruit.pos == snake.parts[-1]:
                if random.randint(0, 1) == 0:
                    fruit = Apple((random.randint(0, 18), random.randint(0, 31)))
                else:
                    fruit = Cherry((random.randint(0, 18), random.randint(0, 31)))
                snake.grow(fruit.consume())

            fruit.update()
            
            snake.draw()
            fruit.draw()
            

            clock.tick(144)
            pygame.display.update()



if __name__ == "__main__":
    app = App()
    app.main()

from collections import deque
from typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}
        self.score = 0

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[-1]

        if direction == "U":
            new_row, new_col = head_row - 1, head_col
        elif direction == "D":
            new_row, new_col = head_row + 1, head_col
        elif direction == "L":
            new_row, new_col = head_row, head_col - 1
        elif direction == "R":
            new_row, new_col = head_row, head_col + 1
        else:
            return -1
        
        if new_row < 0 or new_row >= self.height or new_col < 0 or new_col >= self.width:
            return -1
        
        new_head = (new_row, new_col)
        if new_head in self.snake_set and new_head != self.snake[0]:
            return -1
        
        if self.food and list(new_head) == self.food[0]:
            self.score += 1
            self.food.popleft()
        else:
            tail = self.snake.popleft()
            self.snake_set.remove(tail)
        
        self.snake.append(new_head)
        self.snake_set.add(new_head)

        return self.score
        
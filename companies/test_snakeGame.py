import unittest

from snake_game import SnakeGame

class test_snakeGame(unittest.TestCase):
    def setUp(self):
     # Example setup for the SnakeGame instance
        self.width = 3
        self.height = 2
        self.food = [[1, 2], [0, 1]]
        self.solution = SnakeGame(self.width, self.height, self.food)

    def test_case1(self):
        commands = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
        parameters = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
        expected_outputs = [None, 0, 0, 1, 1, 2, -1]

        game = SnakeGame(*parameters[0])
        for i in range(1, len(commands)):
            if commands[i] == "move":
                self.assertEqual(game.move(*parameters[i]), expected_outputs[i])

    def test_case2(self):
        commands = ["SnakeGame", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move"]
        parameters = [[3, 3, [[2, 0], [0, 0], [0, 2], [0, 1], [2, 2], [0, 1]]], ["D"], ["D"], ["R"], ["U"], ["U"], ["L"], ["D"], ["R"], ["R"], ["U"], ["L"], ["L"], ["D"], ["R"], ["U"]]
        expected_outputs = [None, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, -1]

        game = SnakeGame(*parameters[0])
        for i in range(1, len(commands)):
            if commands[i] == "move":
                self.assertEqual(game.move(*parameters[i]), expected_outputs[i])

if __name__ == '__main__':
    unittest.main()
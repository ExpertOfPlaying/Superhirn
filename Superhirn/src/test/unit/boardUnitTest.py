import unittest
from src.python.entities.boardComponent.board import Board
from src.python.entities.stoneComponent.stone import Stone


class TestBoardClass(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5, 1, [], [], [], 0)
        self.user_input1 = "12345"
        self.user_input2 = "54321"
        self.code_array1 = [int(num) for num in self.user_input1]
        self.code_array2 = [int(num) for num in self.user_input2]
        self.value_list = []
        self.board_stone = [Stone(1), Stone(2), Stone(3), Stone(4), Stone(5)]

    def test_create_board(self):
        self.assertTrue(isinstance(self.board, Board))

    def test_create_board_with_correct_code_max_length(self):
        self.assertEqual(self.board.code_max_length, 5)

    def test_create_board_with_correct_max_colour(self):
        self.assertEqual(self.board.max_colour, 5)

    def test_create_board_with_correct_attempt_counter(self):
        self.assertEqual(self.board.attempt_counter, 1)

    def test_create_board_with_correct_guessed_code(self):
        self.assertEqual(self.board.guessed_code, [])

    def test_create_board_with_correct_code(self):
        self.assertEqual(self.board.code, [])

    def test_create_board_with_correct_feedback(self):
        self.assertEqual(self.board.feedback, [])

    def test_get_game_mode(self):
        self.assertEqual(self.board.game_mode, 0)

    def test_set_max_attempt(self):
        self.board.max_attempt = 20
        self.assertEqual(self.board.max_attempt, 20)

    def test_set_attempt_counter(self):
        self.board.attempt_counter = 10
        self.assertEqual(self.board.attempt_counter, 10)

    def test_set_guessed_code(self):
        self.board.guessed_code = self.code_array1
        self.assertEqual(self.board.convert_stone_array_to_colour(self.board.guessed_code),
                         self.board.convert_stone_array_to_colour(self.board_stone))

    def test_get_guessed_code_list(self):
        self.assertEqual(self.board.guessed_code_list, [])

    def test_add_guessed_code_list(self):
        self.board.guessed_code = self.code_array1
        self.board.guessed_code = self.code_array2
        self.assertEqual(len(self.board.guessed_code_list), 2)

    def test_set_code(self):
        self.board.code = self.code_array1
        self.assertEqual(self.board.convert_stone_array_to_colour(self.board.code),
                         self.board.convert_stone_array_to_colour(self.board_stone))

    def test_set_feedback(self):
        self.board.feedback = self.code_array1
        self.assertEqual(self.board.convert_stone_array_to_colour(self.board.feedback),
                         self.board.convert_stone_array_to_colour(self.board_stone))

    def test_feedback_list(self):
        self.assertEqual(self.board.feedback_list, [])

    def test_set_feedback_list(self):
        self.board.feedback = self.code_array1
        self.board.feedback = self.code_array2
        self.assertEqual(2, len(self.board.feedback_list))


if __name__ == '__main__':
    unittest.main()

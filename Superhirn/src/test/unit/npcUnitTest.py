import unittest

from src.main.python.businesslogic.npcComponent.npc import NPC
from src.main.python.entities.boardComponent.board import Board
from src.main.python.entities.stoneComponent.colourEnum import Colour


class TestNPCClass(unittest.TestCase):

    def setUp(self):
        good_max_code_length_input_string = "5"
        good_max_code_colours = "8"
        bad_stone_input_string = "22334"
        good_stone_input_string = "12345"
        code = "12345"

        self.coder_wrong_guess_board = Board(good_max_code_length_input_string, good_max_code_colours, 1,
                                             "", "", "", 2)
        self.coder_right_guess_board = Board(good_max_code_length_input_string, good_max_code_colours, 1,
                                             "", "", "", 2)

        self.coder_wrong_guess_board.guessed_code = bad_stone_input_string
        self.coder_right_guess_board.guessed_code = good_stone_input_string
        self.coder_wrong_guess_board.code = code
        self.coder_right_guess_board.code = code

        self.npc_coder_winner = NPC(self.coder_wrong_guess_board)
        self.npc_coder_loser = NPC(self.coder_right_guess_board)
        self.npc_guesser_winner = NPC(self.coder_right_guess_board)
        self.npc_guesser_loser = NPC(self.coder_wrong_guess_board)

    def test_npc_feedback_perfect_feedback(self):
        self.npc_coder_loser.generate_feedback()
        npc_feedback_colour = self.coder_right_guess_board.convert_stone_array_to_colour(
            self.coder_right_guess_board.feedback)
        self.coder_right_guess_board.feedback = "88888"
        self.assertEqual(npc_feedback_colour,
                         self.coder_right_guess_board.convert_stone_array_to_colour(
                             self.coder_right_guess_board.feedback))

    def test_npc_feedback_imperfect_feedback1(self):
        self.npc_coder_winner.generate_feedback()
        npc_feedback_colour = self.coder_wrong_guess_board.convert_stone_array_to_colour(
            self.coder_wrong_guess_board.feedback)

        count_white = npc_feedback_colour.count(Colour.WHITE.value)
        count_black = npc_feedback_colour.count(Colour.BLACK.value)

        self.assertEqual(count_white, self.coder_wrong_guess_board.convert_stone_array_to_colour(
            self.coder_wrong_guess_board.feedback).count("7"))
        self.assertEqual(count_black, self.coder_wrong_guess_board.convert_stone_array_to_colour(
            self.coder_wrong_guess_board.feedback).count("8"))

    def test_npc_feedback_imperfect_feedback2(self):
        self.coder_wrong_guess_board.guessed_code = "47654"
        self.test_npc_feedback_imperfect_feedback1()

    def test_calculate_permutations(self):
        for k in range(4, 6):
            for n in range(2, 9):
                self.coder_right_guess_board.code_max_length = k
                self.coder_right_guess_board.max_colour = n
                print(f"{n}^{k}: {self.npc_guesser_winner.generate_permutations()}")


if __name__ == '__main__':
    unittest.main()

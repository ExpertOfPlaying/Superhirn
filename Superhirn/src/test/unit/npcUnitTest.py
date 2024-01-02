import unittest

from src.python.businesslogic.npcComponent.npc import NPC
from src.python.entities.boardComponent.board import Board
from src.python.entities.stoneComponent.colourEnum import Colour
from src.python.businesslogic.npcComponent.npcFeedbackError import NPCFeedbackError


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

        npc_feedback_error = NPCFeedbackError
        self.npc_coder_winner = NPC(self.coder_wrong_guess_board, npc_feedback_error)
        self.npc_coder_loser = NPC(self.coder_right_guess_board, npc_feedback_error)
        self.npc_guesser_winner = NPC(self.coder_right_guess_board, npc_feedback_error)
        self.npc_guesser_loser = NPC(self.coder_wrong_guess_board, npc_feedback_error)

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

    def test_npc_generate_all_permutations(self):
        self.coder_right_guess_board.max_colour = 2
        self.coder_right_guess_board.code_max_length = 4
        min_permutation_array = ['1111', '1112', '1121', '1122', '1211', '1212', '1221', '1222', '2111', '2112',
                                 '2121', '2122', '2211', '2212', '2221', '2222']
        calculated_permutations = self.npc_coder_winner.generate_all_permutations(
            self.coder_right_guess_board.code_max_length,
            self.coder_right_guess_board.max_colour)
        self.assertEqual(min_permutation_array, calculated_permutations)

    def test_npc_variation_feedback(self):
        self.coder_right_guess_board.feedback = "778"
        code_wrong = self.coder_wrong_guess_board.convert_colour_array_to_int(
            self.coder_wrong_guess_board.convert_stone_array_to_colour(self.coder_wrong_guess_board.code))
        code_right = self.coder_right_guess_board.convert_colour_array_to_int(
            self.coder_right_guess_board.convert_stone_array_to_colour(self.coder_right_guess_board.code))

        semi_feedback = [8, 8, 7]
        self.assertEqual(semi_feedback, self.npc_coder_winner.variation_feedback(code_wrong))
        perfect_feedback = [8, 8, 8, 8, 8]
        self.assertEqual(perfect_feedback, self.npc_coder_loser.variation_feedback(code_right))


if __name__ == '__main__':
    unittest.main()

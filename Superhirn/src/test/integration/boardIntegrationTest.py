import unittest


class TestIntegrationBoardClass(unittest.TestCase):
    def mock_test_get_guess_attempt(self):
        start_game()
        role = set_role(rater)
        farben = Stone(7)
        code_length = set_code_length(5)
        self.modus_rater()
        npc.set_code(1, 2, 3, 4, 6)

        board.set_guess(1, 2, 3, 4, 5)
        npc.create_feedback()  # return 7,7,7,7
        board.get_guess()
        ruleBook.validate_guess()
        board.set_feedback()
        board.raise_attempt()
        self.assertEqual(board.get_guess_attempt(), 2)


if __name__ == '__main__':
    unittest.main()

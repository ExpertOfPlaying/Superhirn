import unittest
from src.main.python.businesslogic.roleComponent.menu import Menu
from src.main.python.businesslogic.validatorComponent.gameStateEnum import GameState
from src.main.python.businesslogic.validatorComponent.validationError import ValidationError
from src.main.python.businesslogic.validatorComponent.validator import Validator
from src.main.python.entities.ruleBookComponent.ruleBook import RuleBook
from src.main.python.entities.userComponent.roleEnum import Role
from src.main.python.presentation.terminal import TerminalView


class GameSetupIntegrationTest(unittest.TestCase):
    def setUp(self):
        rule_book = RuleBook
        validation_error = ValidationError
        game_state = GameState
        role = Role
        validator_coder = Validator(rule_book, validation_error, game_state, role.Coder)
        terminal = TerminalView
        self.menu = Menu(validator_coder, terminal)

    def test_game_setup(self):
        self.menu.setup_game()


if __name__ == '__main__':
    unittest.main()

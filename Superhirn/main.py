from src.python.businesslogic.gameControllerComponent.gameController import GameController
from src.python.businesslogic.validatorComponent.gameStateEnum import GameState
from src.python.businesslogic.validatorComponent.validationError import ValidationError
from src.python.businesslogic.validatorComponent.validator import Validator
from src.python.entities.ruleBookComponent.ruleBook import RuleBook
from src.python.entities.userComponent.roleEnum import Role
from src.python.presentation.terminal import TerminalView
from src.python.businesslogic.npcComponent.npcFeedbackError import NPCFeedbackError


def main():
    rule_book = RuleBook
    validation_error = ValidationError
    game_state = GameState
    role = Role
    validator = Validator(rule_book, validation_error, game_state, role)
    terminal = TerminalView
    npc_feedback_error = NPCFeedbackError
    menu = GameController(validator, terminal, npc_feedback_error)
    menu.setup_game()


if __name__ == "__main__":
    main()

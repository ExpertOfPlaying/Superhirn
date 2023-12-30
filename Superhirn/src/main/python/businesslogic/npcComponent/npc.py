import random

from src.main.python.businesslogic.interfaces.observerInterface import Observer
from src.main.python.businesslogic.npcComponent.npcFeedbackError import NPCFeedbackError
from src.main.python.entities.userComponent.roleEnum import Role


class NPC(Observer):
    def __init__(self, board):
        self._board = board
        self._role = self.opposite_role()
        self._all_permutations = self.generate_all_combinations(self._board.code_max_length, self._board.max_colour)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    def opposite_role(self):
        return Role.Coder if self._board.game_mode == Role.Rater.value else Role.Rater

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def update(self, board):
        self._board = board
        if self._role == Role.Coder:
            if not self._board.code:
                self.generate_code()
            else:
                self.generate_feedback()
        elif self._role == Role.Rater:
            self.generate_guess()

    def generate_code(self):
        self._board.code = "".join(
            str(random.randint(1, self._board.max_colour)) for _ in range(self._board.code_max_length))

    def generate_feedback(self):
        feedback = ""
        secret_marked = [False] * len(self._board.code)
        guess_marked = [False] * len(self._board.guessed_code)

        for stone_code_position in range(len(self._board.code)):
            if self._board.code[stone_code_position].colour == self._board.guessed_code[stone_code_position].colour:
                feedback += "8"
                secret_marked[stone_code_position] = guess_marked[stone_code_position] = True

        for stone_code_position in range(len(self._board.code)):
            if not secret_marked[stone_code_position]:
                for stone_guess_position in range(len(self._board.guessed_code)):
                    if (not guess_marked[stone_guess_position]
                            and self._board.code[stone_code_position].colour
                            == self._board.guessed_code[stone_guess_position].colour):
                        feedback += "7"
                        guess_marked[stone_guess_position] = True
                        break

        feedback_list = list(feedback)
        random.shuffle(feedback_list)
        shuffled_feedback = ''.join(feedback_list)
        self._board.feedback = shuffled_feedback

    def generate_permutations(self):
        return pow(self._board.max_colour, self._board.code_max_length)

    def generate_all_combinations(self, code_max_length, max_colour):
        if code_max_length == 0:
            return ['']

        smaller_combinations = self.generate_all_combinations(code_max_length - 1, max_colour)
        combinations = []

        for colour in range(1, max_colour + 1):
            for combination in smaller_combinations:
                combinations.append(str(colour) + combination)

        return combinations

    def variation_feedback(self, solution):
        permutation_feedback = []
        solution_array = []
        solution_copy = []
        guess = self._board.convert_colour_array_to_int(self._board.convert_stone_array_to_colour(self._board.guessed_code))
        for value in solution:
            solution_array.append(int(value))
            solution_copy.append(int(value))

        for i in range(len(guess)):
            if guess[i] == solution_array[i]:
                permutation_feedback.append(8)
                solution_copy[i] = None

        for i in range(len(guess)):
            if guess[i] != solution_array[i] and guess[i] in solution_copy:
                permutation_feedback.append(7)
                solution_copy[solution_copy.index(guess[i])] = None

        return permutation_feedback

    def calculate_nk_value(self, guess):
        remaining_colors = self._board.max_colour - len(set(guess))
        return pow(remaining_colors, self._board.code_max_length)

    @staticmethod
    def count_dopplungen(guess):
        counts = {}
        for color in guess:
            counts[color] = counts.get(color, 0) + 1
        dopplungen = sum(c // 2 for c in counts.values())
        return dopplungen

    def choose_best_guess(self, permutations):
        if not permutations:
            raise NPCFeedbackError("Keine verbleibenden Permutationen. Das Spiel kann nicht fortgesetzt werden.")

        max_dopplungen = max(self.count_dopplungen(guess) for guess in permutations)

        permutationen_mit_max_dopplungen = [guess for guess in permutations if
                                            self.count_dopplungen(guess) == max_dopplungen]

        if permutationen_mit_max_dopplungen:
            min_nk_value = min(self.calculate_nk_value(guess) for guess in permutationen_mit_max_dopplungen)
            beste_permutationen = [guess for guess in permutationen_mit_max_dopplungen if
                                   self.calculate_nk_value(guess) == min_nk_value]
        else:
            min_nk_value = min(self.calculate_nk_value(guess) for guess in permutations)
            beste_permutationen = [guess for guess in permutations if self.calculate_nk_value(guess) == min_nk_value]

        return beste_permutationen[0] if beste_permutationen else None

    def generate_guess(self):
        last_feedback = self._board.convert_colour_array_to_int(self._board.convert_stone_array_to_colour(self._board.feedback))
        self._all_permutations = [permutation for permutation in self._all_permutations if
                                  sorted(self.variation_feedback(permutation)) == sorted(last_feedback)]

        if not self._all_permutations:
            raise NPCFeedbackError("Inkonsistenz im Spielablauf entdeckt. Bitte überprüfe das Benutzerfeedback.")

        self._board.guessed_code = self.choose_best_guess(self._all_permutations)

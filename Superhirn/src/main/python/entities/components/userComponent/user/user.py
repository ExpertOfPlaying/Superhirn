class User:
    def __init__(self, role):
        if role not in ["Rater", "Coder"]:
            raise ValueError("Ungültige Rolle. Bitte wählen Sie 'Rater' oder 'Coder'.")

        self.role = role

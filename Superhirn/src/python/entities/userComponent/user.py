from .roleEnum import Role


class User:
    def __init__(self, role, name):
        self._role = role
        self._name = name

    @property
    def role(self):
        return Role(self._role)

    @role.setter
    def role(self, role):
        self._role = Role(int(role))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

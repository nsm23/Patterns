from copy import deepcopy


class PrototypeMixin:
    """ Prototype паттерн"""

    def clone(self):
        return deepcopy(self)

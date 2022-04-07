from datetime import datetime

from framework_patterns.singleton import SinglePattern


class FrameworkLog(metaclass=SinglePattern):
    """Логгирование"""

    def __init__(self, value):
        self.value = value

    @staticmethod
    def logging(text):
        print(f'log {datetime.now} - ', text)

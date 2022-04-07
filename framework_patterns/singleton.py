class SinglePattern(type):
    """Singleton pattern для реализаии логгирования"""

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            value = args[0]
        if kwargs:
            value = kwargs['value']
        if value in cls.__instance:
            return cls.__instance[value]
        else:
            cls.__instance[value] = super().__init__(*args, **kwargs)
            return cls.__instance[value]

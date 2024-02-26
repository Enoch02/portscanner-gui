class InvalidPortRangeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}'

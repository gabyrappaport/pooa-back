class WritingDataBaseError(Exception):

    def __init__(self, message):
        self.message = message
class SharedBool:
    def __init__(self, initial_value=False):
        self.value = initial_value

    def __bool__(self):
        return self.value

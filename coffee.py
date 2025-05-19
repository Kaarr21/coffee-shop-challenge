class Coffee:
    def __init__ (self, name):
        if isinstance (value, str) and len (value) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")


    @property
    def name (self):
        return self._name

    @name.setter
    def name (self, value):
        raise AttributeError("Coffee name is immutable.")


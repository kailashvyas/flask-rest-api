class Validation:

    @staticmethod
    def is_numeric(value):

        return type(value) == int

    @staticmethod
    def is_in_range(value, min, max):

        return min <= value <= max
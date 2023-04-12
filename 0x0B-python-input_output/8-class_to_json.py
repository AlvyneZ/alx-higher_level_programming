#!/usr/bin/python3
"""
This "8-class_to_json.py" module provides one function:
    class_to_json(obj)
"""


def class_to_json(obj):
    """
    Function that returns a JSON-serializable object from a
     class instance

    Args:
        obj: class instance to be converted

    Returns:
        JSON-serializable object
    """
    return obj.__dict__


if __name__ == "__main__":
    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)


if __name__ == "__main__":
    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number=4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            return "[MyClass] {} - {:d} => {:d}".format(
                self.__name, self.number, self.score
            )

    m = MyClass("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

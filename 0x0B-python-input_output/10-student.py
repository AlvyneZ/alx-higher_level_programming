#!/usr/bin/python3
"""
This "10-student.py" module provides one class:
    Student
"""


class Student:
    """
    Class that defines a rectangle of integer value dimensions

    Attrs:
        self.first_name
        self.last_name
        self.age
        to_json(attrs=None)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializer for setting student details
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a JSON-serializable representation of the instance

        Args:
            attrs: List of attributes to retrieve
        """
        json = self.__dict__.copy()
        if attrs is None:
            return json
        unwanted = set(list(json.keys())).difference(set(attrs))
        for att in unwanted:
            json.pop(att)
        return json


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

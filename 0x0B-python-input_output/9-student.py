#!/usr/bin/python3
"""
This "9-student.py" module provides one class:
    Student
"""


class Student:
    """
    Class that defines a rectangle of integer value dimensions

    Attrs:
        self.first_name
        self.last_name
        self.age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializer for setting student details
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Gets a JSON-serializable representation of the instance
        """
        return self.__dict__


if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))

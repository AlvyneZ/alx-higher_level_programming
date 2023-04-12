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
        if type(attrs) != list:
            return json
        unwanted = set(list(json.keys())).difference(set(attrs))
        for att in unwanted:
            json.pop(att)
        return json

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with data
         in json

        Args:
            json: New data to load into Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)


"""
if __name__ == "__main__":
    import os
    import sys

    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(
        student_1.first_name, student_1.last_name, student_1.age
    ))

    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(
        new_student_1.first_name, new_student_1.last_name, new_student_1.age
    ))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(
        new_student_1.first_name, new_student_1.last_name, new_student_1.age
    ))
"""

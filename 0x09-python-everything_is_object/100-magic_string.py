#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, "n", 1) + 1
    return ", ".join(["BestSchool"] * (magic_string.n - 1))


if __name__ == "__main__":
    for i in range(10):
        print(magic_string())

# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 6: Files
# 03 February 2017


import os
import re


def assignment_6(input1, input2):
    # check for correct filetype
    extension = os.path.splitext(input1)[-1].lower()
    if extension != ".py":
        return -1

    # by using 'with' the files automatically close after dedenting
    # variable i because some comments are not at beginning of line
    with open(input1, "r") as file1, open(input2, "w") as file2:
        for lines in file1:
            comment = lines.strip()
            match = re.search("#", comment)
            if match:
                i = comment.index("#")
                file2.write((comment[i:]).rstrip() + "\n")

    # counting number of comments
    with open(input2, 'r') as file2:
        count = 0
        for lines in file2:
            count += 1
    return count
print(assignment_6("pythonfile1.py", "pythonfile2.py"))

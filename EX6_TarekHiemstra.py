# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 6: Files
# 04 February 2017


import re


def assignment_6(input1, input2):
    # check for correct filetype
    if input1[-3:].lower() != ".py":
        return -1

    # by using 'with' the files automatically close after dedenting
    # variable i because some comments are not at beginning of line
    count = 0
    with open(input1, "r") as file1, open(input2, "w") as file2:
        for lines in file1:
            comment = lines.strip()
            match = re.search("#", comment)
            if match:
                i = comment.index("#")
                file2.write((comment[i:]).rstrip() + "\n")
                count += 1
    return count
#print(assignment_6("pythonfile1.py", "pythonfile2.py"))

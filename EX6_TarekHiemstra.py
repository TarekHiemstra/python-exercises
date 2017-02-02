# Tarek Hiemstra
# Metropolia University of Applied Sciences
# Assignment 6: Files
# 03 February 2017
import os
def assignment_6(input1, input2):
    extension = os.path.splitext(input1)[-1].lower()
    if extension != '.py':
        return -1
# by using 'with' the files automatically close after dedenting
    with open(input1, 'r') as file1, open(input2, 'w') as file2:
        for lines in file1:
            comments = lines.strip()
            if comments.startswith('#'):
                file2.write(comments.rstrip() + '\n')
    with open(input2, 'r') as file2:
        count = 0
        for lines in file2:
            count += 1
    return count
#print(assignment_6('pythonfile1.py', 'pythonfile2.py'))

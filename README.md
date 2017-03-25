# 7 python exercises for the Metropolia course 'Introduction to Programming'

## Assignment 1: Installing the Python Environment
- Install the latest distribution of Python programming environment into your computer. 
- Open IDLE (Integrated Development Environment) for Python. 
- Run the following commands: 
    import platform
    platform
- Copy-paste the contents of the IDLE screen as the answer to this assignment.

## Assignment 2: Variables
Create a Python script, which does the following:
- reads user input for name, age, and your favorite_colour to a list variable
- uses a tuple for constant (string) values
- finds the current date and calculates a lucky number using formula
  ($yourage - $dayofmonth) mod $hour  #(mod = modulo)
- prints a string:
"Hi, my name is $yourname, I'm $yourage years old, and I like $yourfavoritecolour.
Today is $thisdate. 
My lucky number is $luckynumber." 

## Assignment 3: Functions
Write a Python function, which does the following:
- have input parameters: [name, age]
- asks user input for favorite_colour
- uses a tuple for constant (string) values
- finds the current date and calculates a lucky number using formula
  ($yourage - $dayofmonth) mod $hour  #(mod = modulo)
- returns a string:
"Hi, my name is $yourname, I'm $yourage years old, and I like $yourfavoritecolour.
Today is $thisdate. 
My lucky number is $luckynumber."
- Copy and modify the script in the previous assignment to use this function,
  and verify that the original script and modified script with the function work similarly. 
- Add a documentation section to the beginning of the function:
    your name
    Metropolia University of Applied Sciences
    date
    Return the function to this assignment as "EX3_yourname.py" file. 

## Assignment 4: Branches (if)
Make a copy of your Assignment 3 Python function, and modify it to do the following:
- In addition to the Assignment 3, checks the value of $luckynumber and assigns a new variable
    $special = ‘funny’ , if $luckynumber = 0
    ‘normal’ , if $luckynumber is between 1-3
    ‘sunny’ , if $luckynumber is between 4-7
    ‘great’ , if $luckynumber is something else
- Normally function returns a string:
"Hi, my name is $yourname, I'm $yourage years old, and I like $yourfavoritecolour.
Today is $thisdate.
My $special number is $luckynumber."
- Exception: If $hour is greater than or equal to 22, the function should return a string
  "$hour:$minutes: going to sleep now!"
- Note: $anything means the variable you have named yourself (without the dollar sign). I just use this notation to clarify what variables you should show on the result. 
- Modify also the documentation section to the beginning of the function:
    Your name
    Metropolia University of Applied Sciences
    Assignment 4: Branches
    Date
    Return the function to this assignment as "EX4_yourname.py" file.
    
## Assignment 5: Loops
Write a Python function, which does the following:
- Input parameter is a list.
- Checks if all values of a given list are numeric (either int, long, float, or complex). 
- Use for-loop for the test. If there are non-numeric items on the list, exit the function with return value = 0, 
otherwise continue executing function.
- Calculates the sum of the elements until the end of the list or until value is zero, whichever comes first.
  Use while-loop for this part.
- Modify also the documentation section to the beginning of the function:
    Your name
    Metropolia University of Applied Sciences
    Assignment 5: Loops
    Date
- Test the functionality by running the following test sequences:
    Test1 = [1,2,3,4,"5"];  # yourfunction(Test1) should return 0
    Test2 = [1,2,3,4,5];    #should return 15
    Test3 = [1,2,3,4,0,5];  #should return 10
- Return the function to this assignment as "EX5_yourname.py" file.

## Assignment 6: Files
Write a Python function, which saves all Python code comments to a new file:
- Input parameters = two file names
- The first  .py file is opened for reading. The function should first check if the file has correct type
  (.py at the end of filename), and if it is not return from function immediately with return value -1.
- The second .py-file is opened for writing.
- The function goes through the first file and save all comments of it to the second file.
- At the end, it closes both files and returns the number of comments.
- Modify also the documentation section to the beginning of the function:
    Your name
    Metropolia University of Applied Sciences
    Assignment 6: Files
    Date
- Test and return the function to this assignment as "EX6_yourname.py" file.

## Assignment 7: Internet
This exercise uses Weather Underground API, which you can use for free up to 500 calls/day or 10 calls/minute subscription.
You need to register to the service as developer in order to get access to the online data. 
Read carefully the instructions provided in https://www.wunderground.com/weather/api/.
- Write a Python code script, which calls for weather data from Weather Underground service on your date of birth 
on the closest city which provides observations. If you know the exact time of your birth, you may be able to find what
was the weather like when you were born.
- Modify also the documentation section to the beginning of the function:
    Your name
    Metropolia University of Applied Sciences
    Assignment 7: Internet
    Date
    How was the weather when you were born
 - Test and return the function to this assignment as "EX7_yourname.py" file.
 

"""
Loop Counter Module

This module provides functionality to analyze Python source code files and count
the number of for and while loops present in the code. It includes functions
to parse and count different types of loops, helping developers understand the
loop structure of their code.

Functions:
    check_for_loops(lines): Counts the number of for loops in the given code
    check_while_loops(lines): Counts the number of while loops in the given code
    process_a_file(): Main function to process a file and display loop counts

Example:
    To use this module, run it directly:
        $ python bad_refactoring.py
    Then enter the filename when prompted.
"""


# Check for number of for loops in the text
def check_for_loops(lines):
    """ checking for for loops

    Args:
        lines (str): read code as lines

    Returns:
        int: num of for loops exist in the code
    """
    num_for_loops = 0

    for line in lines:
        if line.strip().startswith("for"):
            num_for_loops += 1

    return num_for_loops

# Check for number of while loops in the text
def check_while_loops(lines):
    """checking for while loops

    Args:
        lines (str): read code as lines

    Returns:
        int : num of while loops exist in the code
    """
    num_while_loops = 0

    for line in lines:
        if line.strip().startswith("while"):
            num_while_loops += 1

    return num_while_loops



def process_a_file():
    """
    This is the main function to proces a file for identifying loops in the code 
    
    """

    filename = input("Enter program filename: ")
    lines = open(filename).readlines()

    for_loops = check_for_loops(lines)
    while_loops = check_while_loops(lines)

    print(f"(Program {filename} contain  {for_loops} for loops")
    print(f"(Program {filename} contain  {while_loops} while loops")
    print(f"(Program {filename} contain  {for_loops+while_loops} loops in total")   

process_a_file()

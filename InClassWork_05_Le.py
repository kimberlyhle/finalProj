# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:08:29 2025

@author: kimbe
"""

def rightAngleTri():
    for i in range(0,6):
        print("*" *i)
        
def invertedRAT():
    for i in range(5,0,-1):
        print("*" *i)
        
def pyramid():
    rows = 5  
    for i in range(rows):
        space = rows - i - 1  
        sym = 2 * i + 1        
        print(' ' * space + '$' * sym)
        
def invertedPyra():
    rows = 5
    for i in range(rows):
        space = i
        sym = 2 * (rows - i) - 1
        print(' ' * space + '@' * sym)

def diamond():
    rows = 5
    for i in range(2 * rows - 1):
        if i < rows:
            space = rows - i - 1
            sym = 2 * i + 1
        else:
            space = i - rows + 1
            sym = 2 * (2 * rows - i - 1) - 1
        print(' ' * space + '&' * sym)
        
def square():
    rows = 5
    cols = 5
    for i in range(rows):
        print('%' * cols)

def rotatedRightTri():
    rows = 5
    for i in range(rows):
        space = i  
        sym = rows - i  
        print(' ' * space + '+' * sym)

def main():
    print("\nExecuting Question 1:")
    rightAngleTri()
    print("\nExecuting Question 2:")
    invertedRAT()
    print("\nExecuting Question 3:")
    pyramid()
    print("\nExecuting Question 4:")
    invertedPyra()
    print("\nExecuting Question 5:")
    diamond()
    print("\nExecuting Question 6:")
    square()
    print("\nExecuting Question 8:")
    rotatedRightTri()
    
if __name__ == "__main__":
    main()

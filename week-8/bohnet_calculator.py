#
#============================================
# Title: Assignment 8.3
# Author: Chris Bohnet
# Date: 17 JUne 2020
# Modified By: Chris Bohnet
# Description: Python program with functions to add, subtract and divide.
# Modifications: 
#============================================
#
#function to add 2 numbers
def addTwoNumbers (num1, num2):
    sum=num1+num2;
    return sum;

num1=1
num2=2
print("The sum is", addTwoNumbers(num1, num2));

#function to subtract 2 numbers
def subtractTwoNumbers (num1, num2):
    difference=num1-num2;
    return difference;

num1=4
num2=1
print("The difference is", subtractTwoNumbers(num1, num2));

#function to divide 2 numbers
def divideTwoNumbers (num1, num2):
    quotient=num1/num2;
    return quotient;

num1=8
num2=2
print("The quotient is", divideTwoNumbers(num1, num2));

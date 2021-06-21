#!/usr/bin/env python3

# Created by: Sam. Garcon
# Created on: June 2021
# This program do Number is Positive, Negative or zero

def main():
    # this function do Number is Positive, Negative or zero

    # input
    num = float(input("Enter an integer: "))
    if num > 0:
       print("Positive number")
    elif num == 0:
       print("Zero")
    else:
       print("Negative number")
       
if __name__ == "__main__":
           main()
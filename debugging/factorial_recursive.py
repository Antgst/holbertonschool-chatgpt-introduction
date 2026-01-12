#!/usr/bin/python3
import sys

# =========================
# Function Description
# =========================
# factorial(n) computes the factorial of an integer n using recursion.
# It uses the rule:
#   0! = 1
#   n! = n * (n - 1)! for n > 0
# IMPORTANT: this version assumes n is a non-negative integer (n >= 0).
# If n is negative, the recursion will never reach 0 and will crash.

# =========================
# Parameters
# =========================
# n (int): A non-negative integer whose factorial will be computed.

# =========================
# Returns
# =========================
# int: The factorial of n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# =========================
# Function Description
# =========================
# Reads the first command-line argument, converts it to an integer,
# computes its factorial, then prints the result.
# IMPORTANT: if no argument is provided or if it's not an integer, the program will crash.

# =========================
# Parameters
# =========================
# sys.argv[1] (str): The first command-line argument expected to represent an integer (ideally n >= 0).

# =========================
# Returns
# =========================
# None: Prints the factorial result to standard output.

f = factorial(int(sys.argv[1]))
print(f)

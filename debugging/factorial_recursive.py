#!/usr/bin/python3
import sys

# =========================
# Function Description
# =========================
# factorial(n) computes the factorial of an integer n using recursion.
# It follows:
#   0! = 1
#   n! = n * (n - 1)! for n > 0
# IMPORTANT: this implementation assumes n is a non-negative integer (n >= 0).
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
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)

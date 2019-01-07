#!/usr/bin/env python3

########################################################################
#
# CS 160 - Week 2: Class Fraction
# Purpose: Fractions class with operators.
#
# Author: Ahmad M. Osman
# Date: February 11, 2017
#
# Filename: mOsmanWeek2Ex1.py
#
########################################################################

# Helper function to simplify fractions
def gcd(a, b):
  while a % b != 0:
    tmp = b
    b = a % tmp
    a = tmp
  return b

class Fraction:
  def __init__(self, numer, denom):
    
    if not isinstance(numer, int) or not isinstance(denom, int):
      raise ValueError("Numerator and denominator have to be integers")

    if denom > 0:
      common = gcd(numer, denom)
      self.numer = numer // common
      self.denom = denom // common
    else:
      raise ZeroDivisionError("Denominator must be a positive integer")
    
  def __str__(self):
    return str(self.numer) + '/' + str(self.denom)

  def __eq__(self, other_fraction):
    return self.numer * other_fraction.denom == other_fraction.numer * self.denom

  def __gt__(self, other_fraction):
    if self.numer / self.denom > other_fraction.numer / other_fraction.denom:
      return True
    
  def __add__(self, other_fraction):
    new_numer = self.numer * other_fraction.denom + self.denom * other_fraction.numer
    new_denom = self.denom * other_fraction.denom

    return Fraction(new_numer, new_denom)

  def __sub__(self, other_fraction):
    new_numer = self.numer * other_fraction.denom - self.denom * other_fraction.numer
    new_denom = self.denom * other_fraction.denom
    
    return Fraction(new_numer, new_denom)

  def __mul__(self, other_fraction):
    new_numer = self.numer * other_fraction.numer
    new_denom = self.denom * other_fraction.denom
    
    return Fraction(new_numer, new_denom)

  def __truediv__(self, other_fraction):
    new_numer = self.numer * other_fraction.denom
    new_denom = self.denom * other_fraction.numer
    
    return Fraction(new_numer, new_denom)

  def get_numer(self):
    return self.numer

  def get_denom(self):
    return self.denom

#main function - program execution instructions
def main():
  #Initiation two Fractions
  f1 = Fraction(3, 5)
  print("Fraction 1:", f1)
  f2 = Fraction(4, 7)
  print("Fraction 2:", f2)
  print()

  #Using get_numer() and get_denom()
  print("The numerator of the first fraction is", f1.get_numer(), "and the denominator is", str(f1.get_denom()) + ".")
  print("The numerator of the second fraction is", f2.get_numer(), "and the denominator is", str(f2.get_denom()) + ".")
  print()

  #Addition operator
  f3 = f1 + f2
  print("Addition:", f1, "+", f2, "=", f3)

  #Subtraction operator
  f4 = f1 - f2
  print("Subtraction:", f1, "-", f2, "=", f4)

  #Multiplication operator
  f5 = f1 * f2
  print("Multiplication:", f1, "*", f2, "=", f5)

  #Division
  f6 = f1 / f2
  print("Division:", f1, "/", f2, "=", f6)

  print()

  #Numerator is not an integer
  try:
    f7 = Fraction(5.5, 2)
    print(f7)
  except ValueError as v:
    print(v)

  #Zero division exception
  try:
    f8 = Fraction(5, 0)
    print(f8)
  except ZeroDivisionError as z:
    print(z)

  #Denominator is not an integer
  try:
    f9 = Fraction(5, 2.5)
    print(F9)
  except ValueError as v:
    print(v)

  print()

#Calling main function for program execution
main()
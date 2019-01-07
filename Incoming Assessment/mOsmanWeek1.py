########################################################################
#
# CS 160 - Week 1: Incoming Assessment
# Purpose: Calculating the standard deviation 
#		   of all Fibonacci numbers in a file
#
# Author: Ahmad M. Osman
# Date: February 6, 2017
#
# Filename: mOsmanWeek1.py
#
########################################################################

#Importing math module - needed for sqrt
import math

#Importing random module - needed for randomizing numbers
import random

#A number is Fibonacci for two special cases being perfect square
def is_perfect_square(num):
	square_root_num = int(math.sqrt(num))
	return square_root_num*square_root_num == num

#Finding out if a number is a Fibonacci number
def is_fibonacci(num):
	case_1 = 5*num*num + 4
	case_2 = 5*num*num - 4 

	if(is_perfect_square(case_1) or is_perfect_square(case_2)):
		return True

#Calculating Standard Deviation of a list
def std_deviation(num_list):
	list_avg = sum(num_list) / len(num_list)
	variance = 0

	for item in num_list:
		variance += ((item - list_avg) ** 2)

	std_dev = math.sqrt(variance/len(num_list))

	return std_dev

#Generating 1,000,000 sequenced numbers in a file
def gen_seq_num_file():
    with open('numbers_seq.txt', 'w') as file_out:
        for i in range(10**6):
            file_out.write('%d ' % i)

#Generating 1,000,000 randomized numbers in a file
def gen_rnd_num_file():
    with open('numbers_rnd.txt', 'w') as file_out:
        for i in range(10**6):
            file_out.write('%d ' % random.randint(0, i))

#main function - program execution instructions
def main():
	gen_rnd_num_file()

	with open('numbers_rnd.txt') as file_in:
		numbers = file_in.readline()

	num_list = []
	for num in numbers.split(' '):
		num_list.append(num)
	num_list.pop()
	num_list = [int(num) for num in num_list]

	fibonacci_list = []
	for num in num_list:
		if is_fibonacci(num):
			fibonacci_list.append(num)
	
	std_dev = std_deviation(fibonacci_list)
	print(int(std_dev))

#Calling main function for program execution
main()
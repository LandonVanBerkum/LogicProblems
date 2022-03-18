# Given any integer 1≤n≤100000 not divisible by 2 or 5, some multiple of n is a number which in decimal notation is a sequence of 1’s.
# How many digits are in the smallest such multiple of n? 

import sys

for line in sys.stdin:
	n = int(line.strip())
	counter = 1
	remainder = 1
	while (remainder % n):
		remainder *= 10
		remainder += 1
		remainder %= n
		counter += 1
	print(counter)

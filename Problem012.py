"""
Problem 12 - Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
import math

s = time.time()

num = 1
counter = 1

def get_factors(number):
	factor_count = 0

	if number == 1:
		return 1

	maxrange = int(math.sqrt(number))

	for i in range(1, maxrange + 1):
		if number % i == 0:
			factor_count += 2

	return factor_count


while True:
	num_of_factors = get_factors(num)

	# print(str(num) + " " + str(num_of_factors))

	if num_of_factors + 1 > 500:
		break

	counter += 1
	num += counter

print(num)
print(time.time() - s)

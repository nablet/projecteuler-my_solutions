# Problem 3 - Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from timer import timed


@timed
def problem_003():
    #num = 13195
    num = 600851475143
    primes = []
    i = 2

    while num > 2:
        if num % i == 0:
            primes.append(i)
            num /= i
            i = 2
        else:
            i += 1

    return max(primes)


if __name__ == '__main__':
    print(f"answer: {problem_003()}")

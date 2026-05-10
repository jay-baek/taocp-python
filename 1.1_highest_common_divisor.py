# From p. 2, ch. 1:
# Euclid's algo to find the highest common divisor of two numbers
# i.e., largest number that evenly divides both numbers

import sys

def highest_divisor_of_two_numbers():
	m = int(input("Enter an integer for m: "))
	n = int(input("Enter an integer for n: "))

	if m < n:
		m,n = n,m

	# remainder = True
	counter = 0
	# while(remainder):
	while True:
		r = m%n
		counter += 1
		if r == 0:
			print(f"R{counter}: m/n = {m}/{n} = {m/n}, r = {r}")
			print(f"Highest divisor is: {n}")
			break
		else:
			print(f"R{counter}: m/n = {m}/{n} = {m/n}, r = {r}")
			m, n = n, r


if __name__ == "__main__":
	play = True
	while(play):
		highest_divisor_of_two_numbers()
		play_again = input(f"\nPlay again? [y/n]: ")
		if play_again != "y":
			sys.exit()

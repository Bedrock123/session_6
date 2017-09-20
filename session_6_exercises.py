"""
Zachary Bedrosian
Session 6 Exercises
9.21.2017
"""

"""
1. Write a program, factorial.py to compute a factorial of an integer, n.
"""
def factorial(n):
	"""
	calculates the factorial of the n parameter
	and uses recurstion to find the 
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Run Function
print(factorial(30))


"""
2. Write a program, fibonacci.py to compute the Fibonacci number of an integer , n.
"""
def fibonacci(n):
	"""
	calculates the fibonacci sequence of the n parameter
	and uses recurstion to find the 
	"""
	if n == 0: 
		return 0
	elif n == 1:
		return 1
	else: 
		return fibonacci(n-1)+fibonacci(n-2)

# Run Function
print(fibonacci(10))

def gcd(x, y):
	"""
	calculates the greatest common divisor of the x and y parameters
	reference: https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
	Uses recursion
	"""
	if y == 0:
		return x; 
	else:
		return gcd(y, x%y)

# Run Function
print(gcd(2,12))

"""
4. Implement algorithm for tower of Hanoi. https://www.mathsisfun.com/games/towerofhanoi.html
"""
def move(n, source, bridge, destination):
	if n > 0:
		move(n-1, source, destination, bridge)
		print(source, ' --> ', bridge)
		move(n-1, destination, bridge, source)

print(move(3, 'A', 'B', 'C'))

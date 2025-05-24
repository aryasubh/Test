Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
>>> number = random.randint(1, 100)
>>> guess = None
>>> attempts = 0
>>> while guess != number:
...     guess = int(input("Guess the number between 1 and 100: "))
...     attempts += 1
...     if guess < number:
...         print("Higher!")
...     elif guess > number:
...         print("Lower!")
print(f"Correct! You guessed the number in {attempts} attempts.")

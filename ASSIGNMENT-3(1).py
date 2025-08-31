#METHOD 1

import math
print(math.factorial(5))

#METHOD 2

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(4))

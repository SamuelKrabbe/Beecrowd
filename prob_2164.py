import math

n = float(input())
fib = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / (math.sqrt(5))
print(f"{fib:.1f}")

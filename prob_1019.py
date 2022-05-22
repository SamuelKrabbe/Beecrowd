n = int(input())
m = n // 60
h = m // 60
seconds = n % 60
minutes = m % 60
hours = h

print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

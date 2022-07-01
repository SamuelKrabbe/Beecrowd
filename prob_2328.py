n = int(input())
slices = map(int, input().split())
total_slices = 0

for slice in slices:
    total_slices += slice - 1

print(total_slices)

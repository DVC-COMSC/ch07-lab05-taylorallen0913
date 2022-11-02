strval = input().split()
numbers = []
for v in strval:
	numbers.append(int(v))

target = int(input())

print (numbers)
print(numbers.count(target))
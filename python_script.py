n = int(input())
result = 0
for i in range(0, n):
	value = int(input())
	result = max(result, value)
print("max result = ", result)

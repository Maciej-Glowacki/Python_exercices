num = int(input('Write your number to sum all numbers to the one you wrote: '))

result = 0
for element in range(0, num + 1):
    result = result + element
print(result)

# next option without looping

print(sum(range(0, num + 1)))



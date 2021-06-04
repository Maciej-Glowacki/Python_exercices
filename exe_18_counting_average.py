num = int(input('How many numbers do you want to give? '))

lst = []

while len(lst) < num:
    a = input('Give me the number: ')
    lst.append(a)

result = 0
for element in lst:
    result = result + int(element)

avrg = result / num

if result < avrg:
    print(f'You entered these numbers: {lst}\nSum of your numbers is: {result}\nAverage is: {avrg}\nAverage is higher than sum')
elif result == avrg:
    print(f'You entered these numbers: {lst}\nSum of your numbers is: {result}\nAverage is: {avrg}\nSum and average are equal')
else:
    print(f'You entered these numbers: {lst}\nSum of your numbers is: {result}\nAverage is: {avrg}\nSum is higher than average')

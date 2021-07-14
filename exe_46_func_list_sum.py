def sum_list(numbers):
    return sum(numbers)

print(sum_list([2, 3, 5, 1000]))

def sum_list2(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)
    return result


num_list = [1, 5, 7, 8, 12, 3, 1]
sum_list2(num_list)

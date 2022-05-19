def accepts(num):
    time = []
    for i in range(num, -1, -1):
        time.append(i)
    return time


print(accepts(5))

def print_return(one, two):
    print(one)
    return two

print(print_return(4, 5))

def first_plus_length(three):
    print(three[0])
    num = three[0]

    return len(three) + num

print(first_plus_length([1, 5, 7]))

def values_greater_than_second(four):
    if len(four) < four[1]:
        return False
    new_four = []
    for val in four:
        if val > four[1]:
            new_four.append(val)
    print(len(new_four))
    return new_four

print(values_greater_than_second([5,2,3,2,1,4]))


def this_length_that_value(size, value):
    new_size =[]
    for i in range(size):
        new_size.append(value)
    return new_size
print(this_length_that_value(4, 6))

def countdown(list, num):
    for x in list:
        x *= num
    return list
a = [5,4,3,2,1,0]
b = countdown(a,5)
print(b)

def print_and_return(num):
    print(num[0])
    return(num[1])
print(print_and_return([1,2]))
    
def first_plus_length(num):
    first_value = (num[0])
    length = len(num)
    return first_value + length
print(first_plus_length([2,3,4,5]))

def values_greater_than_second(num):
    num2 = []
    if len(num) < 2:
        return False
    for val in num:
        if val > num [1]:
            num2.append(val)
        print(len(num2))
    return num2
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(num,list):
    num2 = []
    for i in range(num):
        num2.append(list)
    return num2
print(length_and_value(4,7))
print(length_and_value(6,2))
        









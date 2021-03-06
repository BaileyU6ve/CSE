# The Luhn Formula:
#
# See if the numbers are have 16 digits
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10


def validate(num: str):
    if not all_16_digits(num):
        new_list = drop_last_num(num)
        reverse(new_list)
        for i in new_list:
            if not divisible_by_2():
                new_list*2 if i%2 



def all_16_digits(num: str):
    if len(num) == 16:
        print("Everything has 16 digits")


def drop_last_num(num: str):
    list_num = list(num)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
    list_num.pop(15)
    print("The last digit was removed")
    print(list_num)
    return list_num


def reverse(num: str):
    list_num = list(num)
    print(list_num[::-1])


def divisible_by_2(num: str):
    the_num = int(num)
    if the_num % 2 == 0:
        return True
    return False


# def multiply(num: str):
#     the_num = int(num)
#     if divisible_by_2(the_num):
#
#
#
# def subtract(num: str):
#     list_num = list(num)
#     if i in list_num < 9:
#         subtract(9)
#         print(list_num)


print(validate("4556737586899855"))




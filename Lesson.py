
# # HW1

# def say_hi(name: str, age: int):
#        print(f"Hi. My name is {name} and I'm {age} years old")
#
#
# say_hi(name=str(input("Enter name: ")), age=int(input("Enter age: ")))


# HW2

# def correct_sentence(text):
#     text_end = ""
#     if text[-1] != ".":
#         text_end = "."
#         return text[0].upper() + text[1:] + text_end
#     else:
#         return text[0].title() + text[1:]
#
#
# print(correct_sentence("greetings, friends"))
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, Friends.") == "Greetings, Friends.", 'Test4'
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test5'
# print('ОК')


# import string
#
#
# def second_index(text, some_str):
#     my_text = str(text)
#     if my_text.count(some_str) == 1:
#         return None
#     else:
#         return my_text.index(some_str, my_text.index(some_str) + 1)
#
#
# print(second_index("Hello, hello", "lo"))
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# my_list = list(range(0, 101, 1))
# print(my_list)

import random


def common_elements():
    first_numbers = [number for number in range(100) if number % 3 == 0]
    print(first_numbers)
    second_numbers = [number for number in range(100) if number % 5 == 0]
    print(second_numbers)
    return set(first_numbers).intersection(set(second_numbers))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


print(common_elements())
print("ok")


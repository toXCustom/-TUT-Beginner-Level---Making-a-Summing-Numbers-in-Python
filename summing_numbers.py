def sum_function(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

def avg_function(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output/len(numbers)

def word_lenght_function(*strings):
    lenght_list = []

    for string in strings:
        lenght_list += [len(string)]

    shortest = min(lenght_list)
    longest = max(lenght_list)
    average = sum(lenght_list)/len(lenght_list)

    return shortest, longest, average

def sum_ints_function(*objects):
    output = 0

    for obj in objects:
        try:
            output += int(obj)
        except ValueError:
            continue
#        if isinstance(obj, int):
#            output += obj
#        elif isinstance(obj, str):
#            if obj.isdigit():
#                output += int(obj)
    return output

print(sum_function(10, 20, 30, 40))
print(sum_function(3, 7, 5))
print(sum_function(24, 63, 4, 21, 3, 6, 87, 8, 231))
print(avg_function(10, 20, 30, 40))
print(avg_function(3, 7, 5))
print(avg_function(24, 63, 4, 21, 3, 6, 87, 8, 231))
print(word_lenght_function("asd", "loli", "purqua", "Stella"))
print(word_lenght_function("I", "am", "learning", "Python", "slowly"))
print(sum_ints_function(1, "3", 2, 6, "Pawel", "is", "learning"))
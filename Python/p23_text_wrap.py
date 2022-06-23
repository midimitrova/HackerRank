import textwrap

my_string = input()
max_width = int(input())

def my_func(my_string, max_width):
    x = textwrap.wrap(my_string, max_width)
    return "\n".join(x)
print(my_func(my_string, max_width))

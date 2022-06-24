import string

size = int(input())

def my_func(size):
    letters = string.ascii_lowercase

    arr = []

    for i in range(size):
        s = '-'.join(letters[i:size])
        arr.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print('\n'.join(arr[:0:-1] + arr))
my_func(size)
my_string = input()


print(any(x.isalnum() for x in my_string))
print(any(x.isalpha() for x in my_string))
print(any(x.isdigit() for x in my_string))
print(any(x.islower() for x in my_string))
print(any(x.isupper() for x in my_string))




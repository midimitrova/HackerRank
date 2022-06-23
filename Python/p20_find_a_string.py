string = input()
sub_string = input()

count = 0
is_appear = True
start = 0

while is_appear:
    a = string.find(sub_string, start)
    if a == -1:
        is_appear = False
    else:
        count += 1
        start = a + 1
print(count)






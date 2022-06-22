n = int(input())
num_list = map(int, input().split())

my_tuple = tuple(num_list)

print(hash(my_tuple))


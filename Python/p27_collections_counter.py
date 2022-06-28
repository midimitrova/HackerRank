number_size_shoes = int(input())
shoes_size = input().split()
number_customers = int(input())

total_price = 0

for i in range(1, number_customers + 1):
    curr_size, curr_price = input().split()
    if curr_size in shoes_size:
        total_price += int(curr_price)
        shoes_size.remove(curr_size)
print(total_price)




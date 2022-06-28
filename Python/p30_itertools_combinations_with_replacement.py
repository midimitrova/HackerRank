from itertools import combinations_with_replacement

word, number = input().split()

word = sorted(x for x in word)
number = int(number)
result = list(combinations_with_replacement(word, number))
for i in result:
    final_str = ''
    for j in i:
        final_str += j
    print(final_str)

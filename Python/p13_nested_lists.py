number_students = int(input())

full_list = []

for _ in range(1, number_students + 1):
    name = input()
    grade = float(input())

    full_list.append([name, grade])

grades = set()
for name, grade in full_list:
    grades.add(grade)

second_lowest = sorted(list(grades))[1]

lowest_list = []
for name, grade in full_list:
    if grade == second_lowest:
        lowest_list.append(name)

lowest_list.sort()
print('\n'.join(lowest_list))




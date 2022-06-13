n = int(input())

score = map(int, input().split())
all_score = list(score)


all_score_without_dup = list(set(all_score))
all_score_without_dup.sort()
print(all_score_without_dup[-2])





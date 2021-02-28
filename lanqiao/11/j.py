from collections import Counter

holes = []

for i in range(6):
    a, *b = list(map(int, input().split()))
    holes.extend(b)

balls_grade = []
balls_value = []

M = int(input())
for i in range(M):
    a, _, *b = list(map(int, input().split()))
    balls_grade.append(a)
    balls_value.append(b)

holes = Counter(holes)  # 槽位等级计数

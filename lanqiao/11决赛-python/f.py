n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))

jige = list(filter(lambda x: x >= 60, scores))
youxiu = list(filter(lambda x: x >= 85, scores))

jigelv = len(jige) / n
youxiulv = len(youxiu) / n
print(f"{round(jigelv*100)}%")
print(f"{round(youxiulv*100)}%")

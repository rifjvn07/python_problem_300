# 유클리디안 거리
p1 = [0, 0]
p2 = [5, 5]

print(p1, p2)

# root[(b-a)^2+(d-c)^2]
path = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

print(path)

import math

path2 = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
result = math.sqrt(path2)
print(result)

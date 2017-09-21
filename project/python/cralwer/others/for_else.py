import sys

l = list(range(5))

for item in l:
    print(item)
    if item > 5:
        break
else:
    print("5보다 큰 값이 없음")
print("5보다 큰 값이 있음")


# 10871 번

N, X = map(int, input().split())
a = []
a = input().split()
a = list(map(int, a))
for i in range(N) :
    if a[i] < X :
        print(a[i], end = ' ')
    i += 1
import sys

N = int(sys.stdin.readline())
result = [[] for a in range(201)]
for n in range(N):
    row = sys.stdin.readline().split(' ')
    result[int(row[0])].append(row[1])

for idx,i in enumerate(result):
    if i ==[]:
        continue
    elif len(i)>=2:
        for a in i:
            print(idx,a)
    else:
        print(idx,i[0])

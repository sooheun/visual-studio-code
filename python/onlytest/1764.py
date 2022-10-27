import sys

nhear, nsee = map(int, sys.stdin.readline().rstrip().split())

hears = set([sys.stdin.readline().rstrip() for i in range(nhear)])
sees = set([sys.stdin.readline().rstrip() for i in range(nsee)])

same = list(hears & sees)
same = sorted(same)

print(len(same))
for i in same:
    print(i)
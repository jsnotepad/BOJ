import sys

s = sys.stdin.readline().rstrip()
for i in range(ord('a'), ord('z') + 1):
    print(s.find(chr(i)), end=' ')

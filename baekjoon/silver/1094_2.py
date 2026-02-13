import sys

input = sys.stdin.readline

x = int(input())
print(bin(x).count('1'))
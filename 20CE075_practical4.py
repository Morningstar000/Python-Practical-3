# 20CE075 PARTH PARMAR
# Practical 3 Find Captain Room Number
# GitHub link

from collections import Counter

K = int(input())

roomNumbers = map(int, input().split())

freq = Counter(roomNumbers)
for i in freq:
    if freq[i] == 1:
        print(i)

import re

def odd(s):
    n = len(s)
    h = [0] * n
    C = R = 0      # центр и радиус или крайний правый палиндром
    besti, bestj = 0, 0     # центр и радиус самого длинного палиндрома
    for i in range(n):
        j = 0 if i > C+R else min(h[C-(i-C)], C+R-i)
        while i-j > 0 and i+j<n-1 and s[i-j-1] == s[i+j+1]:
            j += 1
        h[i] = j
        if j > bestj:
            besti, bestj = i, j
        if i + j > C + R:
            C, R = i, j
    return s[besti-bestj : besti+bestj+1]

def manacher(s):
    # clean = re.sub('\W ', '', s.lower())
    return odd('|'+'|'.join(s)+'|')[1::2]

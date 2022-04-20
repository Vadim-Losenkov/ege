with open('./24_demo.txt') as f:
    s = f.readline()

k, kmax = 1,1
for i in range(1, len(s)):
    if s[i] == 'Z' and s[i-1] == 'Z': k += 1
    else:
        kmax = max(k, kmax)
        k = 1

print(kmax)
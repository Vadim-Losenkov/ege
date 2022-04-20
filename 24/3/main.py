with open('./24_demo.txt') as file:
    s = file.readline()

k, kmax = 1,1
for i in range(1, len(s)):
    if s[i] == 'Y' and s[i-1] == 'Y': k += 1
    else:
        kmax = max(k, kmax)
        k = 1

print(kmax)
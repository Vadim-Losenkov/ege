with open('./24_demo.txt') as file:
    s = file.readline()

k, kmax = 1,1
for i in range(1, len(s)):
    if s[i] == 'X' and s[i-1] == 'X':
        k += 1
    else:
        kmax = max(k, kmax)
        k = 1

print(kmax)
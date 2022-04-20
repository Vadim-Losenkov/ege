with open('./24_demo.txt') as f:
    s = f.readline()

k, kmax = 3,3
for i in range(2, len(s)):
    if s[i-2] == 'X' and s[i-1] == 'Y' and s[i] == 'Z':
        k += 3
    else:
        kmax = max(k, kmax)
        k = 3

if s[-1] == 'X' or (s[-2] == 'X' and s[-1] == 'Y'): kmax += 1
print(kmax)

# должен получится ответ 13
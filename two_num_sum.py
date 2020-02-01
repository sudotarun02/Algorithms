num = [4, 2, 5, 7, 1, 6, 3]
sum = 10
chk = {}
n = len(num)
for i in range(n):
    req = sum-num[i]
    if num[i] in chk:
        print(chk[num[i]], i)
    else:
        chk[req] = i
n = 5

n2 = (n+3)//2
s = ''.join(map(str,range(1, n2)))

for i in range(n):
    stop = n//2-abs(i-n//2)
    S = s[:stop+1]
    print(S.rjust(n2)+S[-2::-1])





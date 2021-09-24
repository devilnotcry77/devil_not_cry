s = input()
k = len(s)+1
s1 = 'Р'*k
while s.find(s1)==-1:
    k-=1
    s1='Р'*k
print(k)
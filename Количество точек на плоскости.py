
#Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.

lst = []
for i in range(int(input())):
    lst.append(input())
c1 = int() 
c2 = int()
c3 = int()
c4 = int()
for i in lst:
    x, y = i.split(' ')
       
    if x > '0' and y > '0':
        c1 += 1
    elif x < '0' and y > '0':
        c2 += 1
    elif x > '0' and y < '0':
        c4 += 1
    elif x < '0' and y < '0':
        c3 += 1
print("Первая четверть: "+str(c1))
print("Вторая четверть: "+str(c2))
print("Третья четверть: "+str(c3))
print("Четвертая четверть: "+str(c4))


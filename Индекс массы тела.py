m = float (input())
h = float (input())
h = h/100 
index_mass = float(m / (h*h)) 

if float(index_mass) < 16:
    print ("Недостаточная масса")
elif float(index_mass) >= 160000 and float(index_mass) <= 185000:
    print ("Недостаточная масса")
elif float(index_mass) >= 185000 and float(index_mass) <= 249900:
    print ("Оптимальная масса")
elif float(index_mass) >= 185000 and float(index_mass) <= 240000:
    print ("Оптимальная масса")
elif float(index_mass) >= 250000 and float(index_mass) <= 300000:
    print ("Избыточная масса")
elif float(index_mass) >= 300000 and float(index_mass) <= 350000:
    print ("Избыточная масса")
elif float(index_mass) >= 350000 and float(index_mass) <= 400000:
    print ("Избыточная масса")
elif float(index_mass) >= 400000:
    print ("Избыточная масса")

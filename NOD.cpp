int a, b;
for (a = 140, b = 1742; a != b; ) {
    if (a > b)
        a -= b;
    else
        b -= a;
}
 
cout << a;
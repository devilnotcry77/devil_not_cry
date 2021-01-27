#include <iostream>
#include <stdlib.h>
using namespace std;
 
int main() {
    int n; 
    
    // создаем переменную n

    cout << "N = "; 
    
    // выводим сообщение cin >> n; // считываем значение
 
    int res = 1; 
    
    // создаем переменную res

    // в ней мы будем хранить результат работы цикла

    for (int i = 1; i <= n; i++) 
    
    // цикл for

        res *= i; 
        
        // умножаем на i полученное ранее значение
 
    cout << "RES = " << res << endl; 
    
    // выводим результат работы программы
 
    return 0;
}
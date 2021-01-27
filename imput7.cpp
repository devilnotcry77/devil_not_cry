#include <iostream>
using namespace std;
int main()
{
    int i, j, n;
    count<<"Введите число: ";
    cin>>n;
    for (i=1; i<=n; i++)
    {
        for (j=1; j<=n; j++)
        {
            if (i==j)
            count<<i<<"0";
            else
            count<<"0";
        }
        count<<endl;
    }
    return 0;
}

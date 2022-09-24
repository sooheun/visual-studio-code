#include <iostream>
using namespace std;

#include "Circle.h"

int main(void)
{
    Circle r1;
    Circle r2(5);

    cout << "r1의 원 넓이 = " << r1.getArea() << endl;
    cout << "r2의 원 넓이 = " << r2.getArea() << endl;
    
    return 0;
}
#include <iostream>
using namespace std;

class Circle
{

};


int main(void)
{
    int *pInt = new int;
    char *pChar = new char;
    Circle *pCircle = new Circle();

    
    delete pInt;
    delete pChar;
    delete pCircle;

    return 0;
}
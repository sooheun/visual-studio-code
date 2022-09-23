#include <iostream>
#define PI 3.14

using namespace std;

class Circle
{
    int radius;
    public:
        Circle();
        Circle(int r);
        void setRadius(int r);
        double getArea();
        ~Circle();
};

Circle::Circle() : Circle(1) { }

Circle::Circle(int r) : radius(r) { }

void Circle::setRadius(int r)
{
    radius = r;
}

double Circle::getArea()
{
    return PI*radius*radius;
}

Circle::~Circle()
{
    cout << radius << "소멸" << endl;
}

int main()
{
    Circle circleArray[3] = { Circle(10), Circle(20), Circle(30) };
    
    // circleArray[0].setRadius(10);
    // circleArray[1].setRadius(20);
    // circleArray[2].setRadius(30);

    for(int i = 0; i < 3; i++)
    {
        cout << "Circle " << i << "의 면적은 " << circleArray[i].getArea() << endl;
    }

    Circle *p = circleArray;
    for(int i = 0; i < 3; i++)
    {
        cout << "Circle " << i << "의 면적은 " << p[i].getArea() << endl;
    }
}

//p[i].getArea() == (*p).getArea() == p->getArea() 객체 접근에 대한 다양한 방법
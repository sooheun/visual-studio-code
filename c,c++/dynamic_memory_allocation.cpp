#include <iostream>
using namespace std;

class Circle
{
    private:
        double radius;

    public:
        Circle();
        Circle(int);
        void setRadius(double r);
};

void Circle::setRadius(double r)
{
    radius = r;
}

int main(void)
{
    int *pInt = new int;
    char *pChar = new char('a'); // 초기값 설정
    Circle *pCircle = new Circle();

    delete pInt; // 오직 동적 할당 받은 변수만 delete 사용 가능, 중복 반환 안됨
    delete pChar;
    delete pCircle;

    int *p = new int;
    if(!p) // if(p==NULL) 힙 메모리가 부족하면 NULL을 리턴한다, 그러므로 값이 NULL인지 확인
    {
        return 0;
    }
    
    *p = 5;
    int n = *p;
    delete p;

    int *j = new int [5] {1, 2, 3, 4, 5}; // 배열 할당, 반드시 배열의 크기를 지정할 것
    
    if(!j)
    {
        return 0;
    }

    for(int i = 0; i<5; i++)
    {
        j[i] = i; // *(j+i) = i
    }

    delete [] j; // 동적 할당 받은 배열 메모리 반환

    Circle *a = new Circle; // new Circle();
    Circle *b = new Circle(30);

    delete a;
    delete b;

    //객체 배열의 동적 생성, 반환

    Circle *pArray = new Circle[3] { Circle(1), Circle(2), Circle(3)};

    pArray[0].setRadius(10); // 사용 예시


    return 0;
}
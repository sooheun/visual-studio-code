#include <iostream>
using namespace std;

class Circle
{

};


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
        return ;
    }
    *p = 5;
    int n = *p;
    delete p;

    int *j = new int [5]; // 배열 할당
    if(!p)
    {
        return;
    }

    for(int i = 0; i<5; i++)
    {
        p[i] = i;
    }

    delete [] j;


    return 0;
}
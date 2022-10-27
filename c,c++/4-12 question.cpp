#include <iostream>
#include <string>
using namespace std;

class Circle
{
    int radius; // 원의 반지름
    string name; // 원의 이름
    public:
        void setCircle(string name, int radius) {this->radius = radius; this->name = name;} // 이름과 반지름 설정
        double getArea() { return 3.14*radius*radius; }
        string getName() { return name; }
    
};

class CircleManager
{
    Circle *p; // Circle 배열에 대한 포인터
    int size; // 배열의 크기
    public:
        CircleManager(int size); //size 크기의 배열을 동적 생성. 사용자로부터 입력 완료
        ~CircleManager() {delete [] p;}
        void searchByName(); // 사용자로부터 원의 이름을 입력받아 면적 출력
        void searchByArea(); // 사용자로부터 원의 면적을 입력받아 면적보다 큰 원의 이름 출력
};

CircleManager::CircleManager(int size)// 배열 생성, 원의 정보 입력
{
    string name;
    int r;
    this -> size = size;
    p = new Circle[size];
    for(int i = 0; i < size; i++)
    {
        cout << "원 " << i+1 <<"의 이름과 반지름 >> ";
        cin >> name >> r;
        p[i].setCircle(name, r);
    }
}

void CircleManager::searchByName() // 원의 이름을 입력받고 그 원의 넓이를 출력함
{
    string find_name;
    cout << "검색하고자 하는 원의 이름 >> ";
    cin >> find_name;
    
    for(int i = 0; i < size; i++)
    {
        if (p[i].getName() == find_name)
        {
            cout << find_name <<"의 면적은 " << p[i].getArea() << endl;
        }
    }
}

void CircleManager::searchByArea() // 원의 넓이를 입력받고 그 넓이 보다 큰 원을 출력함
{
    int find_area;
    cout << "최소 면적을 정수로 입력하세요 >> ";
    cin >> find_area;
    
    cout << find_area << "보다 큰 원을 검색합니다." << endl;
    for(int i = 0; i < size; i++)
    {
        if (p[i].getArea() > find_area)
        {
            cout << p[i].getName() <<"의 면적은 " << p[i].getArea() << ",";
        }
    }

}

int main(void)
{
    int size;
    cout << "원의 개수 >> ";
    cin >> size;

    CircleManager *Cir = new CircleManager(size);
    Cir->searchByName();
	Cir->searchByArea();
    
    return 0;
}
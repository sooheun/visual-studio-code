#include <iostream>
#include <string>
using namespace std;

class Circle
{
    int radius; // ���� ������
    string name; // ���� �̸�
    public:
        void setCircle(string name, int radius) {this->radius = radius; this->name = name;} // �̸��� ������ ����
        double getArea() { return 3.14*radius*radius; }
        string getName() { return name; }
    
};

class CircleManager
{
    Circle *p; // Circle �迭�� ���� ������
    int size; // �迭�� ũ��
    public:
        CircleManager(int size); //size ũ���� �迭�� ���� ����. ����ڷκ��� �Է� �Ϸ�
        ~CircleManager() {delete [] p;}
        void searchByName(); // ����ڷκ��� ���� �̸��� �Է¹޾� ���� ���
        void searchByArea(); // ����ڷκ��� ���� ������ �Է¹޾� �������� ū ���� �̸� ���
};

CircleManager::CircleManager(int size)// �迭 ����, ���� ���� �Է�
{
    string name;
    int r;
    this -> size = size;
    p = new Circle[size];
    for(int i = 0; i < size; i++)
    {
        cout << "�� " << i+1 <<"�� �̸��� ������ >> ";
        cin >> name >> r;
        p[i].setCircle(name, r);
    }
}

void CircleManager::searchByName() // ���� �̸��� �Է¹ް� �� ���� ���̸� �����
{
    string find_name;
    cout << "�˻��ϰ��� �ϴ� ���� �̸� >> ";
    cin >> find_name;
    
    for(int i = 0; i < size; i++)
    {
        if (p[i].getName() == find_name)
        {
            cout << find_name <<"�� ������ " << p[i].getArea() << endl;
        }
    }
}

void CircleManager::searchByArea() // ���� ���̸� �Է¹ް� �� ���� ���� ū ���� �����
{
    int find_area;
    cout << "�ּ� ������ ������ �Է��ϼ��� >> ";
    cin >> find_area;
    
    cout << find_area << "���� ū ���� �˻��մϴ�." << endl;
    for(int i = 0; i < size; i++)
    {
        if (p[i].getArea() > find_area)
        {
            cout << p[i].getName() <<"�� ������ " << p[i].getArea() << ",";
        }
    }

}

int main(void)
{
    int size;
    cout << "���� ���� >> ";
    cin >> size;

    CircleManager *Cir = new CircleManager(size);
    Cir->searchByName();
	Cir->searchByArea();
    
    return 0;
}
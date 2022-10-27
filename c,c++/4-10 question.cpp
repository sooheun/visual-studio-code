#include <iostream>
#include <string>

using namespace std;

class Person
{
	string name;
	public:
		Person() { };
		Person(string name) { this->name = name; }
		void set_name_num(string name) { this->name = name; }
		string getName() { return name; }
};

class Family
{
	Person *p;
	int size;
	string family_name;
	public:
		Family(string name, int size);
		void setName(int number, string name);
		void show();
		~Family() { delete [] p; } // family Ŭ���� ����� �Ҹ��ڸ� ������� PersonŬ������ �޸� ��ȯ ����
};

Family::Family(string name, int size) // size�� ���� person ���� �迭, �����, ���� �̸� ����
{
	p = new Person[size];
	this->size = size;
	family_name = name;
}

void Family::setName(int number, string name) // size��ŭ ��ȣ�� ����� �Է¹ް� ��ȣ�� �´� �迭�� ����� �̸��� ������
{
	p[number].set_name_num(name);
}

void Family::show() // ���� �������� �����
{
	cout << family_name << " ������ ������ ���� " << size <<"�� �Դϴ�." << endl;
	for(int i = 0; i < size; i++)
	{
		cout << p[i].getName() <<"\t";
	}
}

int main(void)
{
	Family *simpson = new Family("Simpson", 3);
	simpson->setName(0, "Mr. Simposn");
	simpson->setName(1, "Mrs. Simposn");
	simpson->setName(2, "Bart Simpson");
	simpson->show();
	
	delete simpson;

	return 0;
}

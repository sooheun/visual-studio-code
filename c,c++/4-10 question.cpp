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
		~Family() { delete [] p; } // family 클래스 종료시 소멸자를 실행시켜 Person클래스의 메모리 반환 실행
};

Family::Family(string name, int size) // size에 따라 person 동적 배열, 사람수, 가족 이름 설정
{
	p = new Person[size];
	this->size = size;
	family_name = name;
}

void Family::setName(int number, string name) // size만큼 번호와 사람을 입력받고 번호에 맞는 배열에 사람의 이름을 저장함
{
	p[number].set_name_num(name);
}

void Family::show() // 가족 구성원을 출력함
{
	cout << family_name << " 가족은 다음과 같이 " << size <<"명 입니다." << endl;
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

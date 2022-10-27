#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string> 
using namespace std;

class Book
{
    string title; // å �̸�
    int price; // ����
public:
    Book(const string title, int price);
    ~Book() { };
    void set(const string title, int price);
    void show() { cout << title << ' ' << price << "��" << endl; }
};

Book::Book(string title, int price)
{
    this->price = price;
    this->title = title;
}

void Book::set(const string title, int price)
{
    this->price = price;
    this->title = title;
}

int main(void)
{
    Book cpp("��ǰC++", 10000);
    Book java = cpp; // ��������� ����
    java.set("��ǰ�ڹ�", 12000);
    cpp.show();
    java.show();

    return 0;
}
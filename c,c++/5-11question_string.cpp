#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string> 
using namespace std;

class Book
{
    string title; // 책 이름
    int price; // 가격
public:
    Book(const string title, int price);
    ~Book() { };
    void set(const string title, int price);
    void show() { cout << title << ' ' << price << "원" << endl; }
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
    Book cpp("명품C++", 10000);
    Book java = cpp; // 복사생성자 실행
    java.set("명품자바", 12000);
    cpp.show();
    java.show();

    return 0;
}
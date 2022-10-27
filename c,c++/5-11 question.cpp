#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring> 
using namespace std;

class Book
{
    char* title; // 책 이름
    int price; // 가격
public:
    Book(const char* title, int price);
    Book(const Book& book); // 깊은 복사 생성자
    ~Book();
    void set(const char* title, int price);
    void show() { cout << title << ' ' << price << "원" << endl; }
};

Book::Book(const char* title, int price)
{
    this->price = price;
    int len = strlen(title);
    this->title = new char [len + 1];
    strcpy(this->title, title);
}

Book::Book(const Book& book)
{
    this->price = book.price;
    int len = strlen(book.title);
    this->title = new char[len + 1];
    strcpy(this->title, book.title);
}

Book::~Book()
{
    delete[] title;
}

void Book::set(const char* title, int price)
{
    if (this->title) // 메모리가 할당되어 있으면 반환하고 다시 받는다. 
    {
        delete[] this->title;
    }
    this->price = price;
    int len = strlen(title);
    this->title = new char [len + 1];
    strcpy(this->title, title);
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
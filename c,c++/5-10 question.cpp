#include <iostream>
#include <string>
using namespace std;

class Buffer
{
    string text;
    public:
        Buffer(string text) { this->text = text; }
        void add(string next) { text += next;}
        void print() { cout << text << endl; }

};

Buffer& append(Buffer& p, string name)
{
    p.add(name);
    return p;
}

int main(void)
{
    Buffer buf("Hello");
    Buffer& temp = append(buf, "Guys");
    temp.print();
    buf.print();
    return 0;
}
#include <iostream>
using namespace std;

class Dept
{
    int size;
    int* scores;
public:
    Dept(int size)
    {
        this->size = size;
        scores = new int[size];
    }
    //Dept(const Dept& dept);
    ~Dept() { delete[] scores; };
    int getSize() { return size; }
    void read();
    bool isOver60(int index);
};

// Dept::Dept(const Dept& dept)
// {
//     this -> size = dept.size;
//     this -> scores = new int[size];
//     for(int i = 0; i < 10; i++)
//     {
//         this->scores[i] = dept.scores[i];
//     }
// }

void Dept::read()
{
    cout << "10개 점수 입력>> ";
    for (int i = 0; i < 10; i++)
    {
        cin >> scores[i];
    }
}

bool Dept::isOver60(int index)
{
    if (scores[index] >= 60)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int countPass(Dept dept) // 문제 3번 의 답 -> int countPass(Dept &dept)
{
    int count = 0;
    for (int i = 0; i < dept.getSize(); i++)
    {
        if (dept.isOver60(i)) count++;
    }
    return count;
}

int main(void)
{
    Dept com(10);
    com.read(); // 10명의 성적 입력후 저장
    int n = countPass(com);
    cout << "60점 이상은 " << n << "명";
    return 0;
}
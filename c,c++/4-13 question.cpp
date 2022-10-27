#include <iostream>
#include <string>
#include <locale> //�빮�� �Ǻ�, ���ĺ��Ǻ� ���� �Լ��� ����
using namespace std;

class Histogram
{
    string sentence;
    public:
        Histogram(string sent) { sentence = sent; cout << sent << endl;}
        void put(string sent) { sentence += sent; cout << sent;}
        void putc(char c) { sentence += c; cout << c;}
        void print();
};

void Histogram::print()
{
    int cnt = 0; //���ĺ��� ������ �� ����
    int al[26] = { 0 }; // a~z �� ������ ���� �迭
    
    for(int i = 0; i < sentence.length() ; i++)
    {
        if (isalpha(sentence[i])) // �� ���ڿ��� �ƽ�Ű�ڵ� ���� �̿��Ѵ�.
        {
            al[tolower(sentence[i]) -'a'] += 1; // tolower() -> �빮�ڸ� �ҹ��ڷ� �ٲ�
            cnt += 1;
        }
    }
    cout << endl << endl;
    cout << "�� ���ĺ� �� "<< cnt << endl << endl;

    
    for(int i = 0; i < 26; ++i)
    {
        char alpha = 'a' + i;
		cout << alpha << " (" << al[i] << ")" << "\t: ";
        for(int j = 0; j < al[i]; ++j)
        {
            cout << "*";
        }
        cout << endl;
        alpha = alpha + 1;
    }


}

int main(void)
{
    Histogram elvisHisto("Wise men say, only fools rush in But I can't help, ");
    elvisHisto.put("falling in love with you");
    elvisHisto.putc('-');
    elvisHisto.put("Elvis Presley");
    elvisHisto.print();

    return 0;
}
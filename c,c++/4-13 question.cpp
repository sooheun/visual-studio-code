#include <iostream>
#include <string>
#include <locale> //대문자 판별, 알파벳판별 등의 함수가 있음
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
    int cnt = 0; //알파벳의 개수를 셀 변수
    int al[26] = { 0 }; // a~z 의 개수를 담을 배열
    
    for(int i = 0; i < sentence.length() ; i++)
    {
        if (isalpha(sentence[i])) // 각 문자열의 아스키코드 값을 이용한다.
        {
            al[tolower(sentence[i]) -'a'] += 1; // tolower() -> 대문자를 소문자로 바꿈
            cnt += 1;
        }
    }
    cout << endl << endl;
    cout << "총 알파벳 수 "<< cnt << endl << endl;

    
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
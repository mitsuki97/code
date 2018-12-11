#include <iostream>
using namespace std;
int main()
{
    long int num;
    int place;
    void ten_thousand(int);
    void thousand(int);
    void hundred(int);
    void ten(int);
    void indiv(int);
    cout << "enter an integer(0~99999)";
    cin >> num;
    if (num > 9999)
        place = 5;
    else if (num > 999)
        place = 4;
    else if (num > 99)
        place = 3;
    else if (num > 9)
        place = 2;
    else
        place = 1;
    cout << "place=" << place << endl;
    ten_thousand(num);
    thousand(num);
    hundred(num);
    ten(num);
    indiv(num);
    cout << "original order:" << ten_thousand << thousand << hundred << ten << indiv << endl;
    switch (place)
    {
    case 5:
        cout << ten_thousand << "," << thousand << "," << hundred << "," << ten << "," << indiv << endl;
        cout << "rever order";
        cout << indiv << ten << hundred << thousand << ten_thousand << endl;
        break;
    case 4:
        cout << thousand << "," << hundred << "," << ten << "," << indiv << endl;
        cout << "rever order";
        cout << indiv << ten << hundred << thousand << endl;
        break;
    case 3:
        cout << hundred << "," << ten << "," << indiv << endl;
        cout << "rever order";
        cout << indiv << ten << hundred << endl;
        break;
    case 2:
        cout << ten << "," << indiv << endl;
        cout << "rever order";
        cout << indiv << ten << endl;
        break;
    case 1:
        cout << indiv << endl;
        cout << "rever order";
        cout << indiv << endl;
        break;
    }
    return 0;
}

void ten_thousand(int num);
{
    ten_thousand = num / 10000;
}
void thousand(int num);
{
    thousand = (int num)(num - ten_thousand * 10000) / 1000;
}
void hundred(int num);
{
    hundred = (int num)(num - ten_thousand * 10000 - thousand * 1000) / 100;
}
void ten(int num);
{
    ten = (int)(num - ten_thousand * 10000 - thousand * 1000 - hundred * 100) / 10;
}
void indiv(int num);
{
    indiv = (int)(num - ten_thousand * 10000 - thousand * 1000 - hundred * 100 - ten * 10);
}
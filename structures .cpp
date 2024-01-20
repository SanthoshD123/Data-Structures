#include <iostream>
using namespace std;

struct Rectangle{
    int length;
    int breadth;
};
int main()
{
    struct Rectangle r;
    r.length = 15;
    r.breadth = 10;
    cout << r.length*r.breadth << endl;

    return 0;
}

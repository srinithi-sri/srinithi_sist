#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    int r;
    while(n!=0)
    {
        int temp = n%10;
        r= temp*10 +temp;
        n /=10;
    }
    cout<<r;
    return 0;
}

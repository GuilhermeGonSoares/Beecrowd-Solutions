#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    
    int a;
    float b;
    char c;
    string frase;
    
    cin >> a >> b >> c;
    cin.ignore();
    getline(cin, frase);
    cout << a << fixed << b << c << frase << endl;
    cout << a << "\t" << fixed << b << "\t" << c << "\t" << frase << endl;
    cout << setw(10) << a << setw(10) << fixed << b << setw(10) << c << setw(10) << frase << endl;

    return 0;
}
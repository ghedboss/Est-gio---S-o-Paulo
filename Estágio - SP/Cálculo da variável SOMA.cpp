#include <iostream>

using namespace std;

int main() {
    int INDICE = 13;
    int SOMA = 0;
    int K = 0;

    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }

    cout << SOMA << endl;
    return 0;
}

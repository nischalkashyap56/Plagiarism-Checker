#include <stdio.h>

void fibonacci(int n) {
    int a = 0, b = 1, nextTerm;

    printf("Fibonacci series up to %d terms:\n", n);
    for (int i = 1; i <= n; ++i) {
        printf("%d ", a);
        nextTerm = a + b;
        a = b;
        b = nextTerm;
    }
    printf("\n");
}

int main() {
    int n = 10; // Change the value of n to get a different number of Fibonacci series elements

    fibonacci(n);

    return 0;
}
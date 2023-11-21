#include <stdio.h>

void fibonacci(int n) {
    int fib[n + 2];
    int i;

    fib[0] = 0;
    fib[1] = 1;

    printf("Fibonacci series up to %d terms:\n", n);
    printf("%d %d ", fib[0], fib[1]);

    for (i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
        printf("%d ", fib[i]);
    }
    printf("\n");
}

int main() {
    int n = 10; // Change the value of n to get a different number of Fibonacci series elements

    fibonacci(n);

    return 0;
}
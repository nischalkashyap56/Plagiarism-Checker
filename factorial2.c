#include <stdio.h>

// Function to calculate the factorial iteratively
unsigned long long factorial(int n) {
    if (n < 0) {
        return 0; // Factorial is not defined for negative numbers
    }

    unsigned long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int num;
    
    printf("Enter a positive integer: ");
    scanf("%d", &num);

    unsigned long long result = factorial(num);

    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d = %llu\n", num, result);
    }

    return 0;
}
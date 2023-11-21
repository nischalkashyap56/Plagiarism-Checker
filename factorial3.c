#include <stdio.h>

// Function to calculate the factorial using memoization
unsigned long long memo[21]; // Storing factorials up to 20

unsigned long long factorial(int n) {
    if (n < 0) {
        return 0; // Factorial is not defined for negative numbers
    }

    if (n <= 1) {
        return 1;
    }

    if (memo[n] != 0) {
        return memo[n]; // If the factorial is already calculated, return it
    }

    memo[n] = n * factorial(n - 1); // Calculate and memoize the factorial
    return memo[n];
}

int main() {
    int num;

    printf("Enter a positive integer (up to 20): ");
    scanf("%d", &num);

    if (num < 0 || num > 20) {
        printf("Factorial is not defined for negative numbers or numbers greater than 20.\n");
    } else {
        unsigned long long result = factorial(num);
        printf("Factorial of %d = %llu\n", num, result);
    }

    return 0;
}

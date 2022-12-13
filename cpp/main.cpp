#include <iostream>

// Function to calculate the sum of two numbers
int sum(int num1, int num2) {
return num1 + num2;
}

int main() {
int i = 0; // Initialize variable for loop
int result = 0; // Initialize variable to hold sum of numbers

// Loop through numbers 1-10 and add to result
for (i = 1; i <= 10; i++) {
result = sum(result, i);
}

// If result is greater than 20, print "Result is greater than 20"
if (result > 20) {
std::cout << "Result is greater than 20" << std::endl;
}

return 0;
}

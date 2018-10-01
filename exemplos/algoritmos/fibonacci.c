#include <stdio.h>
#include <stdlib.h>

int fibonacci (int n);
int recursiveFibonacci (int n);


int main () {
  printf("Sequência usando o fibonacci sem recursão\n");
	for (int i = 0; i < 20; i++) {
		printf("%d ", fibonacci(i));
	}
  
  printf("\n\nSequência usando o fibonacci recursivo\n");
	for (int i = 0; i < 20; i++) {
		printf("%d ", recursiveFibonacci(i));
	}

	printf("\n");
  return 0;
}


int fibonacci (int n) {
	int sequence[n + 1];
	sequence[0] = 0;
	sequence[1] = 1;

	for (int i = 2; i <= n; i++) {
		sequence[i] = sequence[i - 1] + sequence[i - 2];
	}

	return sequence[n];
}


int recursiveFibonacci (int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
  }
}

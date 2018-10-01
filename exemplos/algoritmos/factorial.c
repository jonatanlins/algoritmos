#include <stdio.h>

int factorial (int n);
int recursiveFactorial (int n);


int main () {
  printf("Sequência usando o fatorial sem recursão\n");
	for (int i = 0; i < 10; i++) {
		printf("%d ", factorial(i));
	}
	
  printf("\n\nSequência usando o fatorial recursivo\n");
	for (int i = 0; i < 10; i++) {
		printf("%d ", recursiveFactorial(i));
	}

	printf("\n");
	return 0;
}


int factorial (int n) {
	int i = 1;
	while (n > 0) {
		i *= n;
		n--;
	}
	return i;
}


int recursiveFactorial (int n) {
	return (n == 0) ? 1 : (n * recursiveFactorial(n - 1));
}

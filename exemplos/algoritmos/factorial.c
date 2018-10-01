#include <stdio.h>

int factorial (int n) {
	int i = 1;
	while (n > 0) {
		i *= n;
		n--;
	}
	return i;
}

int main () {
	for (int i = 0; i < 10; i++) {
		printf("%d ", factorial(i));
	}

	printf("\n");

	return 0;
}

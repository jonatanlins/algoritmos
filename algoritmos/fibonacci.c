#include <stdio.h>
#include <stdlib.h>

int fibonacci (int n);

void main () {
	for (int i = 0; i < 20; i++) {
		printf("%d ", fibonacci(i));
	}

	printf("\n");
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

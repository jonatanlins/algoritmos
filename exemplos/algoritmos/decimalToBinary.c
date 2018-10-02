#include <stdio.h>
#include <stdlib.h>

// OBSERVAÇÂO:
// Esse código não funciona com número grandes e tem alguns problemas
// ele serve apenas como exemplo, não deve ser usado em uma aplicação real

int decimalToBinary (int decimal);


int main () {

	int number;

	printf("Digite um número em base decimal: ");
	scanf("%d", &number);
	
	printf("\nDecimal: %d\n", number);
	printf("Binário: %d\n", decimalToBinary(number));

	return 0;
}


int decimalToBinary (int decimal) {
	int binary = 0, i = 1;

	while (decimal) {
		binary += i * (decimal % 2);
		i *= 10;
		decimal /= 2;
	}

	return binary;
}

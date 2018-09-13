// Dado um limite inferior e superior, imprima e calcule a soma
// de todos os números primos contidos nesse intervalo.

#include <stdio.h>
#include <stdlib.h>

int isPrime (int num);

void main () {
  int min, max;

  printf("Qual o limite inferior? ");
  scanf("%d", &min);
  printf("E o limite superior? ");
  scanf("%d", &max);

  if (min > max) {
    printf("Você digitou os números errados seu babaca!\n");
    printf("O limite inferior tem que ser menor que o superior.\n");
    exit(0);
  }

  int counter = 0;

  for (int i = min; i <= max; i++) {
    if (isPrime(i)) {
      counter += i;
    }
  }

  printf("A soma dos números primos é %d\n", counter);
}

int isPrime (int num) {
  // Função que recebe um número e verifica se ele é primo
  if (num <= 1) return 0;
  if (num % 2 == 0 && num > 2) return 0;
  for (int i = 3; i < num / 2; i += 2) {
    if (num % i == 0) {
      return 0;
    }
  }
  return 1;
}

// Ler vários números até obter o finalizador 0.
// Indicar quantos números quadrados perfeitos, ou seja,
// números que têm raiz quadrada inteira, foram lidos.

#include <stdio.h>
#include <stdlib.h>

int isPerfectSquare (int num);

void main () {
  int counter = 0;

  while (1) {
    int num;

    scanf("%d", &num);
    if (num == 0) {
      printf("\nVocê digitou %d quadrados perfeitos.\n", counter);
      exit(0);
    }

    if (isPerfectSquare(num)) {
      counter++;
    }
  }
}

int isPerfectSquare (int num) {
  // Função que recebe um número e verifica se ele é quadrado perfeito
  for (int i = 1; i <= num / 2 + 1; i++) {
    if (num == i * i) {
      return 1;
    }
  }
  return 0;
}

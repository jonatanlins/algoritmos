// Uma das maneiras de se conseguir a raiz quadrada de um número é
// subtrair dele os números ímpares consecutivos a partir de 1,
// até que o resultado seja menor ou igual a zero.
// O número de vezes que se conseguir fazer as subtrações é a raiz quadrada.
// Faça um algoritmo que calcule a raiz quadrada de dado número conforme essa regra.

#include <stdio.h>

void main () {
  int num, counter = 0;

  printf("Digite um número: ");
  scanf("%d", &num);
  printf("\nA raiz quadrada de %d é ", num);

  for (int i = 1; num > 0; i += 2) {
    num -= i;
    counter++;
  }

  printf("%d\n", counter);
}

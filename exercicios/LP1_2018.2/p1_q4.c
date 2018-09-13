// Escreva uma função recursiva chama "potencia", que aceite dois parâmetros
// inteiros positivos i e j. A função retorna i elevado à potência j.
// Por exemplo: potencia(2, 3) = 8.
// Use a seguinte definição: i^j = i^(j - 1) * i

#include <stdio.h>

int potencia (int i, int j) {
  return (j == 0) ? 1 : (i * potencia(i, j - 1));
}

void main () {
  int i, j;

  printf("Digite o número i: ");
  scanf("%d", &i);
  printf("Digite o número j: ");
  scanf("%d", &j);

  printf("%d elevado à potência %d é igual a %d\n", i, j, potencia(i, j));
}

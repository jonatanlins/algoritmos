#include <stdio.h>

// Não existe uma forma simples de obter o tamanho de uma array dentro de uma função
// A maneira mais fácil é usando uma macro
#define arrayLength(array) (sizeof(array) / sizeof(array[0]))

void main () {
  int array[20];
  char string[50];

  printf("o comprimento do vetor é: %d\n", arrayLength(array));
  printf("o comprimento da string é: %d\n", arrayLength(string));
}
